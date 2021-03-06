from abcust.celery import app
from abcust.settings import AUDREY_MAC_ADDRESS
from abcust.lib.audrey import Audrey
from abcust.tasks import slack


def notify(message):
    slack.write.delay('Audrey', 'good', message=message, log=True)


@app.task
def power_on():
    audrey = Audrey(AUDREY_MAC_ADDRESS, debug=True)
    audrey.send_command('TOGGLE:POWER:ON')
    audrey.disconnect()
    notify('파워모드를 켰습니다.')


@app.task
def power_off():
    audrey = Audrey(AUDREY_MAC_ADDRESS, debug=True)
    audrey.send_command('NORMAL:COOL:27:LOW')
    audrey.disconnect()
    notify('파워모드를 껐습니다.')


@app.task
def turn_on():
    audrey = Audrey(AUDREY_MAC_ADDRESS, debug=True)
    audrey.send_command('ON')
    audrey.disconnect()
    notify('에어컨을 켰습니다.')


@app.task
def turn_off():
    audrey = Audrey(AUDREY_MAC_ADDRESS, debug=True)
    audrey.send_command('OFF')
    audrey.disconnect()
    notify('에어컨을 껐습니다.')


@app.task
def raw_command(command):
    audrey = Audrey(AUDREY_MAC_ADDRESS, debug=True)
    audrey.send_command(command)
    audrey.disconnect()
    notify('다음 명령을 받았습니다: {}'.format(command))
