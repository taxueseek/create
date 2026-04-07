#!/usr/bin/env python3
"""首次安装检测：menu_server.py 缺失时自动重建。"""
import os, textwrap

base = os.path.dirname(os.path.abspath(__file__))
server_path = os.path.join(base, 'menu_server.py')
html_path   = os.path.join(base, 'menu.html')

if not os.path.exists(server_path):
    open(server_path, 'w').write(textwrap.dedent(r"""
        #!/usr/bin/env python3
        \"\"\"Taxue CLI menu — terminal-based router, no browser, no port needed.\"\"\"
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
                if choice.startswith("/"):
                    print(choice)
                else:
                    print("custom:" + choice)

        if __name__ == "__main__":
            main()
    """).strip())
    print('created menu_server.py')

if not os.path.exists(html_path):
    print('ERROR: menu.html missing — reinstall skill from repo')
    exit(1)

print('ok')
