from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util import number

c = int("0x402f29a8a6f71fe10a07872276b0f400769a53552d376c0f7b48244c6da0cda16ab8ce861c3d56a8b940601b9193a4f139c068522f3e57f4453be3120c4a0c3074b81d55ea013cc70325f61e63f23b282ead222dc311faca08c6c354e09d2383e41834c6f9600ab82439aef6a94907a468733ba902c67859e3bc0cdc3f503ee",16)
d_part = "0x0b6bc0230f44e5f0125ea62d5d2f0e302465ae77efdda8182c9567c767faeaa84c8cf74c4fe9dc61371590b7424c3c4a6fa3987758cf28904c9fa0d943c6eac797381b65af3d222af2b03b5de73dba3aac449156883913fad396851b35c9c7285b741ccb37308d5953863157fbf80203f6cebc94c1b470b8e7404b9fcbca"
n = int("0xd9775a6b997779d1da49c4976c64076a520b637167a97ecfb2054084ac2c0ac37fe74b945a7e68a3123bf3d37c59b4df509e6edff4492db6234e3bff1de77a633908ce824cb4d04e6bb01fe4c7e7c98aa6b7cf936adb00843b081e7c9f83445e5f4af1f35de7bcfc9e33cd546852790911573962b0088b3d96fae474c9cbb8e1",16)

def safe_decode(b: bytes) -> str:
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return None
    
for x in range(2**16):
    d = int(d_part + format(x,"x"),16)
    m = pow(c, d, n)
    pt = long_to_bytes(m)
    decoded = safe_decode(pt)
    
    if decoded is not None:
        if "CSEC" in decoded:
            print(decoded)
            print(format(d, "x")) 