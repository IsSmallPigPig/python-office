from office.api.markdown import *


class TestMarkdown():
    # def test_markdown_link_image_to_base64(self, ):
    #     # TODO:提交测试文档
    #     markdown_link_image_to_base64(
    #         markdown_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\markdown\test.md")
    #
    # def test_check_local_dir_image_link_markdown(self):
    #     # TODO:提交测试文档
    #     check_local_dir_image_link_markdown(
    #         markdown_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\markdown\test.md",
    #         image_path=r"C:\Users\37386\PycharmProjects\python-office\testfile\markdown\test.assets")
    def test_excel2markdown(self):
        excel2markdown(input_file=r'../test_files/excel/fake2excel.xlsx', output_file=r'../test_files/markdown/test.md',
                       sheet_name=None)
