import sys
import click

from scrap_cointool import scrap
# from metaMask import add_wallet

@click.command()
@click.argument('path')
@click.argument('id')
@click.option('--count', '-c', default=1, help='Count of wallets created')
@click.option('--type', '-t', default='eth', help='Type of cryptocurrency. You can get type in url cointool /createWallet/[TYPE]')
def main(path, id, count, type):
    data = scrap(type, count)
    print(data)


if __name__ == '__main__':
    main()


