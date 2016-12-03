from app import create_app
from flask import Manager, Shell

app = create_app('default')
manager = Manager()


def make_shell_context():
    """
    Context for shell
    :return:
    """
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
