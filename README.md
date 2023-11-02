# BB84 Algorithm Simulation Overview

The BB84 protocol is a quantum key distribution method developed by Charles Bennett and Gilles Brassard in 1984. It enables two parties to securely exchange cryptographic keys using the principles of quantum mechanics.

The provided code is a Python simulation based on the BB84 protocol. The protocol allows two parties, traditionally named Alice and Bob, to securely exchange a secret key by using the properties of quantum mechanics.

## Protocol Explanation

**Quantum Bits (Qubits) Generation (Alice) :**
- Alice generates a stream of qubits in random states (0 or 1) and encodes each qubit with one of two possible bases: either the rectilinear basis (+, x) or the diagonal basis (↗, ↖).
- The choice of basis for encoding the qubits is random for each qubit.

 **Eavesdropping (Eve):**
   - The code simulates the possibility of an eavesdropper, Eve, intercepting the qubits sent from Alice to Bob.
   - Eve also randomly chooses the bases to measure the qubits, and based on that choice, she may or may not change the state of the qubit.
   - Eve's interference can potentially disrupt the transmission and be detected by Alice and Bob.
     
**Qubits Measurement (Bob):**
   - Bob receives the qubits from Alice, but some qubits might have been intercepted and altered by Eve. Bob randomly chooses a basis to measure each qubit.
   - If Bob guesses the same basis that Alice used to encode the qubit, he will obtain the correct value.
   - Otherwise, Bob's measurement outcome might not match what Alice sent.

**Comparison and Error Detection:**
   - Alice and Bob publicly announce the bases they used for encoding and decoding the qubits. They discard measurements where Bob used a different basis than Alice.
   - Then, they compare a subset of their results to check for errors. If a significant number of bits do not match (usually 25%), it indicates the possible presence of an eavesdropper.

