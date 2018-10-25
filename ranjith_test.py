#!/usr/bin/env python3


import sys
from argparse import ArgumentParser
from subprocess import Popen, PIPE
import random
from threading import Thread, Condition
import signal
import os


def generate_expr(max_len):
  """
  :param int max_len:
  :return: random expression
  :rtype: str
  """
  if max_len <= 3:
    return random.choice(list("0123456789"))
  s = ""
  while True:
    if s and random.random() < 0.2:  # stop now?
      return s
    new_s = s
    sub_expr_require_non_zero = False
    if s:
      new_s += random.choice(list("+-*/"))
      if new_s[-1] == "/":
        sub_expr_require_non_zero = True
    if random.random() < 0.2:  # sub expression?
      try:
        sub_expr = generate_expr(max_len=max(max_len // 2, 1))
      except RecursionError:
        sub_expr = "42"
      if sub_expr_require_non_zero and eval_expr(sub_expr) == 0:
        continue  # just try again
      new_s += "(%s)" % sub_expr
    else:  # some number
      if not sub_expr_require_non_zero and random.random() < 0.1:  # zero
        new_s += "0"
      else:  # non-zero
        new_s += random.choice(list("123456789"))
        # Some random len. Prefer shorter.
        if random.random() < 0.7:
          num_str_len = random.randint(0, 3)
        else:
          num_str_len = random.randint(0, 10)
        for i in range(num_str_len):
          new_s += random.choice(list("0123456789"))
    if len(new_s) > max_len:
      if s:
        return s
      # Just try again.
    else:
      s = new_s


def eval_expr(s):
  """
  :param str s:
  :return: solution
  :rtype: int
  """
  # Of course, this is not how your solution is allowed to look like.
  # You must not use eval. But of course, we can here, for the sake of testing the solution.
  # To make it a valid Python expression, replace all "/" by "//".
  s = s.replace("/", "//")
  return eval(s)


class TimeoutChecker(Thread):
  def __init__(self, proc, timeout):
    """
    :param Popen proc:
    :param float timeout: in seconds
    """
    super(TimeoutChecker, self).__init__(name="TimeoutChecker")
    self.proc = proc
    self.timeout = timeout
    self.cond = Condition()
    self.daemon = True
    self.notified = False
    self.start()

  def notify(self):
    with self.cond:
      self.notified = True
      self.cond.notify()

  def run(self):
    with self.cond:
      if self.notified:  # maybe already now
        return
      self.cond.wait(self.timeout)
      if self.notified:
        return
    print("Error: Timeout.")
    self.proc.send_signal(signal.SIGINT)


def main():
  arg_parser = ArgumentParser()
  arg_parser.add_argument("--exec", default="solution.py", help="your Python solution.py")
  arg_parser.add_argument("--num_tests", default=100, type=int, help="number of tests to run")
  arg_parser.add_argument("--expr_max_len", default=100, help="max len for expr")
  arg_parser.add_argument("--timeout", default=5.0, type=float, help="timeout for each expression")
  arg_parser.add_argument("--seed", default=42, type=int, help="random seed")
  args = arg_parser.parse_args()
  random.seed(args.seed)
  os.environ["PYTHONUNBUFFERED"] = "1"
  proc = Popen(["python3", args.exec], stdin=PIPE, stdout=PIPE, bufsize=0)
  for n in range(args.num_tests):
    # We assume that the solution consumes all input until newline, so we should not have a blocking problem.
    expr = generate_expr(max_len=args.expr_max_len)
    res = eval_expr(expr)
    print("Testing %s = %i." % (expr, res))
    timeout_checker = TimeoutChecker(proc=proc, timeout=args.timeout)
    proc.stdin.write(("%s\n" % expr).encode("utf8"))
    proc.stdin.flush()
    solution_res_bytes = proc.stdout.readline()
    timeout_checker.notify()
    proc.poll()
    if proc.returncode is not None:  # terminated
      print("Error, solution terminated (return code %i)." % proc.returncode)
      sys.exit(1)
    solution_res = int(solution_res_bytes.decode("utf8"))
    if solution_res == res:
      print("  Solution correct.")
    else:
      print("  Solution wrong! (%i)" % solution_res)
      sys.exit(1)
  proc.stdin.close()
  proc.wait()


if __name__ == "__main__":
  import better_exchook
  better_exchook.install()
  try:
    main()
  except KeyboardInterrupt:
    print("KeyboardInterrupt")
    sys.exit(1)
