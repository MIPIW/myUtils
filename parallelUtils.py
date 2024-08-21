class ParallelUtils:

    import multiprocessing

    def __init__(self):
        self.type = None
        self.func = None

        pass

    # pre_assign: whether the function runs with pandas.map or pandas.apply or not
    def do_series(self, series, num_cores, pre_assign=False):

        from multiprocessing import Pool
        import numpy as np
        import pandas as pd

        if num_cores == 1:  ##############somewhere error occurs
            if not pre_assign:
                return self._assign_map(series)
            else:
                return self.func(series)

        se_split = np.array_split(series, num_cores)
        pool = Pool(num_cores)
        if not pre_assign:
            df = pd.concat(pool.map(self._assign_map, se_split))
        else:
            df = pd.concat(pool.map(self.func, se_split))
        pool.close()
        pool.join()

        return df

    def _assign_map(self, serie):
        return serie.progress_map(self.func)

    def _assign_apply(self, df, axis):
        return df.progress_apply(self.func, axis=axis)

    def change_function(self, func):
        self.func = func

    def do_dataFrame(self, df, num_cores, axis=None, pre_assign=False):
        from multiprocessing import Pool
        import numpy as np
        import pandas as pd
        from functools import partial

        if num_cores == 1:
            if not pre_assign:
                if axis == None:
                    return ValueError("axis needed")
                return self._assign_apply(df, axis=axis)
            else:
                return self.func(df)

        se_split = np.array_split(df, num_cores)
        pool = Pool(num_cores)
        if not pre_assign:

            if axis == None:
                return ValueError("axis needed")

            f = partial(self._assign_apply, axis=axis)
            df = pd.concat(pool.map(f, se_split))

        else:
            df = pd.concat(pool.map(self.func, se_split))
        pool.close()
        pool.join()

        return df
