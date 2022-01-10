from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucscoreutils import get_meta_info

# Create a connection handle
handle = UcsHandle("ip.or.fqdn.ofucs", "username", "pa$$w0rd")

# Login to the server
handle.login()

#print blade information
blades = handle.query_classid("computeBlade")
print(len(blades))
for blade in blades:
    print(blade.model,blade.serial,blade.dn)

#logout from server
handle.logout()

