def test(alice_secret, bob_secret):
    g = 23
    p = 5

    alice_key = (p**alice_secret) % g
    bob_key = (p**bob_secret) % g
    shared_key_1 = (alice_key**bob_secret) % g
    shared_key_2 = (bob_key**alice_secret) % g
    print('sk1: {}\tsk2: {}'.format(shared_key_1, shared_key_2))

test(4, 3)
