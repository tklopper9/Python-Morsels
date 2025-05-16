def add(*A):   
    A_, *A_res = A
    nrows = len(A_)
    ncols = len(A_[0])

    for a in A_res:
        if (len(a) != nrows):
            raise ValueError("Given matrices are not the same size.")
        for a_ in a:
            if (len(a_) != ncols):
                raise ValueError("Given matrices are not the same size.")

    for a in A_res:
      A_ = [[x + y for x, y in zip(A_[i], a[i])] for i, _ in enumerate(A_)]

    return A_