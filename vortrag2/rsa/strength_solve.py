## WRITE UP PLAID CTF 2015: strength
__author__ = 'h0rst'

# https://github.com/hellman/libnum
from libnum import *


def read_data(file_name):
    # Data format: {N_i : e_i : c_i}
    data = []
    with open(file_name)as lines:
        next(lines)
        for line in lines:
            [N, e_i, c_i] = line[1:-2].split(" : ")
            # drop the '0x' and store as 'long'
            [N, e_i, c_i] = [long(N[2:],16), long(e_i[2:],16), long(c_i[2:],16)]
            data.append([N, e_i, c_i])
        return data


def find_tuple(data):
    # find tuple (e_i, e_j) with  gcd(e_i, e_j) == 1
    # It is expected that N_i == N_j  for all i,j
    for i in xrange(len(data)):
        N_i, e_i, c_i = data[i]
        for j in xrange(len(data)):
            N_j, e_j, c_j = data[j]
            if gcd(e_i, e_j) == 1 :
                return N_i, e_i, c_i, e_j, c_j
    print "No tuple found!"
    exit(1)


def decrypt(N, e_1, c_1,  e_2, c_2):
                # find x, y so that  g = 1 = e_1 * x + e_2 * y
                x, y ,g = xgcd(e_1, e_2)

                # Let x < 0 : c^x = c^(-1*|x|) = (c^-1)^|x|
                if x < 0 :
                    c_1 = invmod(c_1, N)
                    x *= -1

                if y < 0 :
                    c_2 = invmod(c_2, N)
                    y *= -1

                # m = m^1 = m^(e_1*x + e_2*y) = (m^e_1)^x * (m^e_1)^y = c_1^x * c_2^y (mod N)
                m = (pow(c_1, x, N) * pow(c_2, y, N)) % N
                return hex(m)[2:-1].decode('hex')


## MAIN:
N, e_1, c_1, e_2, c_2 = find_tuple(read_data('./captured_827a1815859149337d928a8a2c88f89f'))
print decrypt(N, e_1, c_1, e_2, c_2)
