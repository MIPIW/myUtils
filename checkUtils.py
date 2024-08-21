class CheckUtils:
    def __init__(self) -> None:
        pass

    # def checkValue(func):
    #     from functools import partial
    #     partial
    @staticmethod
    def checkSeries(
        serdf,
        isNan=True,
        isEmpty=True,
        isInf=True,
        isNotInstance=None,
        isNotIn=False,
        isNotInVal=None,
        type="row",
    ):
        import pandas as pd
        import math

        def _check_subsequent(
            x,
            isNotInstance=isNotInstance,
            isNan=isNan,
            isEmpty=isEmpty,
            isInf=isInf,
            isnotIn=isNotIn,
            isNotInVal=isNotInVal,
        ):
            out = False

            if isNotInstance is not None:
                x1 = not isinstance(x, isNotInstance)
            else:
                x1 = False

            if isinstance(x, (int, float, complex)):
                x2 = pd.isna(x) if isNan else False
                x3 = math.isinf(x) if isInf else False
                x4 = False

            elif x == None:
                x2 = False
                x3 = False
                x4 = True if isEmpty else False

            else:
                x2 = False
                x3 = False
                x4 = (len(x) == 0) if isEmpty else False

            x5 = isNotInVal not in x if isNotIn else False

            return out | x1 | x2 | x3 | x4 | x5

        if isinstance(serdf, pd.Series):
            return serdf.progress_map(_check_subsequent)

        elif isinstance(serdf, pd.DataFrame):
            out = serdf.map(_check_subsequent)  # cellwise
            if type == "row":
                return out.apply(lambda x: any(x), axis=1)
            if type == "col":
                return out.apply(lambda x: any(x), axis=0)

        else:
            raise ValueError("this is not either series or dataframe.")

    @staticmethod
    def isEmpty(dataframe) -> bool:

        if len(dataframe.index) == 0:
            return True

        return False
