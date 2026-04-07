#!/usr/bin/env python3
"""Taxue CLI menu — terminal-based router, no browser, no port needed."""
import sys

MENU = [
    ("1", "/think",     "想不清楚、纠结、不确定、选哪个"),
    ("2", "/solve",     "怎么办、出错了、卡住了、要解法"),
    ("3", "/breakdown", "事情太多、怎么拆解、怎么安排"),
    ("4", "/search",    "搜一下、查一下、信息不够"),
    ("5", "/learn",     "怎么学、想学会、想掌握"),
    ("6", "/build",     "重复做、做模板、建流程"),
    ("7", "/roundtable","多角度、专家讨论、开圆桌"),
]

def print_menu():
    print("\n踏雪寻仙 | 选一个最贴近你现在的状态：\n")
    for num, cmd, desc in MENU:
        print(f"  [{num}] {cmd:12s} — {desc}")
    print("\n  [q] 退出")
    print("")

def main():
    print_menu()
    try:
        choice = input("输入编号 (1-7): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

    mapping = {num: cmd for num, cmd, _ in MENU}
    if choice in mapping:
        print(mapping[choice])
    elif choice in ("q", "quit", "exit"):
        sys.exit(0)
    else:
        # Fallback: if user typed a command directly (e.g. "/think"), pass it through
        if choice.startswith("/"):
            print(choice)
        else:
            print("custom:" + choice)

if __name__ == "__main__":
    main()
