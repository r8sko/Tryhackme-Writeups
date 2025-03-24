from sympy import factorint, mod_inverse

n=340282366920938460843936948965011886881
e=65537

def eulers_tontient(p, q):
    result = (p-1) * (q-1)
    return result



def find_p_and_q(n):

    "Because n = p * q"

    primes = factorint(n)

    p, q = primes.keys()

    return [p, q]

list_p_q = find_p_and_q(n)

p = list_p_q[0]

q = list_p_q[1]

e_result = eulers_tontient(p,q)

private_exponent = mod_inverse(e, e_result)

print("This is the private key: ",private_exponent) 