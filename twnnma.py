##under going

#tensor product
# np.einsum looks best
np.einsum('ijk,jin->kn',a,b)
#
np.tensordot(a,b,axes=([2],[0]))
# lazy mode or @ 3.5
np.matmul(a, b) 

#Python 3.5
a @ b

# np.kron
# np.dot as it calls DGEMM from a BLAS library.

# TensorFlow
# tf.einsum('ijk,jin->kn',a,b)
# tf.matmul(a, b)
# tf.svd(tensor, full_matrices=False, compute_uv=True, name=None)
# tf.sqrt(x, name=None)
