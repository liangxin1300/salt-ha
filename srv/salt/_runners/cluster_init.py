
import logging
import salt.client
import salt.output.no_out

log = logging.getLogger(__name__)


def get_ips(**kwargs):
    local = salt.client.LocalClient()
    res = local.cmd('*', 'grains.get', ['ipv4'])
    salt.output.no_out.output(res)
    return "1111"
