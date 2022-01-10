# Requires python3 and ucssdk installed

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucscoreutils import get_meta_info

# Create a connection handle
handle = UcsHandle("ip.or.fqdn.ofucs", "username", "pa$$w0rd")

# Login to the server
handle.login()


#
#██╗░░░██╗░█████╗░██╗░░░██╗██████╗░  ░█████╗░░█████╗░██████╗░███████╗
#╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝
#░╚████╔╝░██║░░██║██║░░░██║██████╔╝  ██║░░╚═╝██║░░██║██║░░██║█████╗░░
#░░╚██╔╝░░██║░░██║██║░░░██║██╔══██╗  ██║░░██╗██║░░██║██║░░██║██╔══╝░░
#░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║  ╚█████╔╝╚█████╔╝██████╔╝███████╗
#░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚═════╝░╚══════╝
#
#
#



#logout from server
handle.logout()
