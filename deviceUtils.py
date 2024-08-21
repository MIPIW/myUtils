class DeviceUtils:

    @staticmethod
    def gpu_usage():
        import nvidia_smi

        nvidia_smi.nvmlInit()
        deviceCount = nvidia_smi.nvmlDeviceGetCount()
        lst = []
        for i in range(deviceCount):
            handle = nvidia_smi.nvmlDeviceGetHandleByIndex(i)
            mem = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
            lst.append(
                f"|Device {i}| Mem Free: {mem.free/1024**2:5.2f}MB / {mem.total/1024**2:5.2f}MB"
                + f"(used: {(mem.total/1024**2 - mem.free/1024**2):5.2f}MB, {round((mem.total/1024**2 - mem.free/1024**2) / (mem.total/1024**2) * 100, 1)}%)",
            )
        return lst

    @staticmethod
    def empty_gpu(*, args_list, delete=False):
        import gc, time, torch

        for i in args_list:
            if delete:
                del i
        gc.collect()
        torch.cuda.empty_cache()
        for i in range(5):
            time.sleep(1)
            print(f"{i} of 5")
        return DeviceUtil.gpu_usage()

    @staticmethod
    def gpu_usage_decorator(func):
        def wrapper(args):

            x = func(*args)

            print(DeviceUtils.gpu_usage())

            return x

        return wrapper
