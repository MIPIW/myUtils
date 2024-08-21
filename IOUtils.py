class IOUtils:
    def __init__(self):
        pass

    @staticmethod
    def existsFile(file_url):
        from pathlib import Path

        if isinstance(file_url, str):
            url = Path(file_url).resolve()
        else:
            url = file_url.resolve()

        if url.exists():
            c = 1
            while True:
                if Path(
                    str(url.parent) + "/" + str(url.stem) + f"_{c}" + str(url.suffix)
                ).exists():
                    c += 1
                else:
                    break

            print(
                f"The file already exists. The url of the fIle to be saved is {url} + number"
            )

            return Path(
                str(url.parent) + "/" + str(url.stem) + f"_{c}" + str(url.suffix)
            )

        print(f"The url of the fIle to be saved is {url}")
        return url

    @staticmethod
    def recentFile(file_url):

        from pathlib import Path

        if type(file_url) == str:
            url = Path(file_url).resolve()
        else:
            url = file_url.resolve()

        if url.exists():
            c = 1
            while True:
                if Path(
                    str(url.parent) + "/" + str(url.stem) + f"_{c}" + str(url.suffix)
                ).exists():
                    c += 1
                else:
                    break
        else:
            c = 0
        if c == 0:
            return f"File not exists in {url}"

        if c == 1:
            print(
                f'The url of the fIle to be loaded is {Path(str(url.parent) + "/" + str(url.stem + str(url.suffix)))}'
            )
            return Path(str(url.parent) + "/" + str(url.stem + str(url.suffix)))
        else:
            print(
                f'The url of the fIle to be loaded is {Path(str(url.parent) + "/" + str(url.stem + f"_{c-1}" + str(url.suffix)))}'
            )
            return Path(
                str(url.parent) + "/" + str(url.stem + f"_{c-1}" + str(url.suffix))
            )

    # 굳이?
    # @staticmethod
    # def checkpoint_save(
    #     file_path, data, data_type="dataFrame", file_type="csv", index_dataFrame=False
    # ):
    #     import json

    #     save_path = IOUtils.existsFile(file_path)

    #     if data_type == "dataFrame" or data_type == "series":
    #         import pandas as pd

    #         if file_type == "csv":
    #             data.to_csv(save_path, index=index_dataFrame, encoding="utf-8")

    #     if data_type == "list":
    #         if file_type == "txt":
    #             with open(save_path, "w", encoding="utf-8") as f:
    #                 for item in data:
    #                     f.write(item)
    #                     f.write("\n")

    #         if file_type == "jsonl":

    #             with open(save_path, "w", encoding="utf-8") as f:
    #                 for item in data.items():
    #                     f.write(json.dumps(item))
    #                     f.write("\n")

    #     if data_type == "dict":
    #         if file_type == "json":

    #             with open(save_path, "w", encoding="utf-8") as f:
    #                 json.dump(data, f, indent="\t")

    #     return data  # for the neatness of the code

    # @staticmethod
    # def checkpoint_load(file_path, data_type="dataFrame", file_type="csv"):

    #     import json

    #     load_path = IOUtils.recentFile(file_path)

    #     if data_type == "dataFrame" or data_type == "series":
    #         import pandas as pd

    #         if file_type == "csv":
    #             out = pd.read_csv(load_path)
    #             return out

    #     if data_type == "list":
    #         if file_type == "txt":
    #             out = None

    #             with open(load_path, "r", encoding="utf-8") as f:
    #                 out = [i.strip() for i in f.readlines()]
    #             return out

    #         if file_type == "jsonl":
    #             out = []

    #             with open(load_path, "r", encoding="utf-8") as f:
    #                 for line in f:
    #                     out.append(json.loads(line))

    #             return out

    #     if data_type == "dict":
    #         if file_type == "json":

    #             out = None

    #             with open(load_path, "r", encoding="utf-8") as f:
    #                 out = json.loads(f)

    #             return out
