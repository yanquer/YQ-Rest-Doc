===============
OCR识别
===============

OCR (Optical Character Recognition), 光学字符识别

简单baidu了一下, 看到了一篇 `几种python入门级OCR开源库中文识别效果对比 <https://blog.csdn.net/coderider/article/details/126886577>`_

作者推荐使用 PaddleOCR

安装::

  pip install paddlepaddle shapely paddleocr

例:

演示图片:

.. figure:: ../../../../resources/images/2023-03-16-11-35-21.png
  :width: 480px

代码::

  def ocr_with_paddle(img: str) -> list:
      from paddleocr import PaddleOCR, draw_ocr

      ocr_pad = PaddleOCR(use_angle_cls=True, lang="ch")
      result = ocr_pad.ocr(img, cls=True)
      return result


  if __name__ == '__main__':
      _img = './img.png'
      r = ocr_with_paddle(_img)
      for x in r:
          for y in x:
              print(y)

      for x in r:
          for y in x:
              print(y[1][0])

结果::

  [2023/03/16 11:34:21] ppocr DEBUG: Namespace(help='==SUPPRESS==', use_gpu=False, use_xpu=False, use_npu=False, ir_optim=True, use_tensorrt=False, min_subgraph_size=15, precision='fp32', gpu_mem=500, image_dir=None, page_num=0, det_algorithm='DB', det_model_dir='/Users/yanque/.paddleocr/whl/det/ch/ch_PP-OCRv3_det_infer', det_limit_side_len=960, det_limit_type='max', det_box_type='quad', det_db_thresh=0.3, det_db_box_thresh=0.6, det_db_unclip_ratio=1.5, max_batch_size=10, use_dilation=False, det_db_score_mode='fast', det_east_score_thresh=0.8, det_east_cover_thresh=0.1, det_east_nms_thresh=0.2, det_sast_score_thresh=0.5, det_sast_nms_thresh=0.2, det_pse_thresh=0, det_pse_box_thresh=0.85, det_pse_min_area=16, det_pse_scale=1, scales=[8, 16, 32], alpha=1.0, beta=1.0, fourier_degree=5, rec_algorithm='SVTR_LCNet', rec_model_dir='/Users/yanque/.paddleocr/whl/rec/ch/ch_PP-OCRv3_rec_infer', rec_image_inverse=True, rec_image_shape='3, 48, 320', rec_batch_num=6, max_text_length=25, rec_char_dict_path='/usr/local/lib/python3.9/site-packages/paddleocr/ppocr/utils/ppocr_keys_v1.txt', use_space_char=True, vis_font_path='./doc/fonts/simfang.ttf', drop_score=0.5, e2e_algorithm='PGNet', e2e_model_dir=None, e2e_limit_side_len=768, e2e_limit_type='max', e2e_pgnet_score_thresh=0.5, e2e_char_dict_path='./ppocr/utils/ic15_dict.txt', e2e_pgnet_valid_set='totaltext', e2e_pgnet_mode='fast', use_angle_cls=True, cls_model_dir='/Users/yanque/.paddleocr/whl/cls/ch_ppocr_mobile_v2.0_cls_infer', cls_image_shape='3, 48, 192', label_list=['0', '180'], cls_batch_num=6, cls_thresh=0.9, enable_mkldnn=False, cpu_threads=10, use_pdserving=False, warmup=False, sr_model_dir=None, sr_image_shape='3, 32, 128', sr_batch_num=1, draw_img_save_dir='./inference_results', save_crop_res=False, crop_res_save_dir='./output', use_mp=False, total_process_num=1, process_id=0, benchmark=False, save_log_path='./log_output/', show_log=True, use_onnx=False, output='./output', table_max_len=488, table_algorithm='TableAttn', table_model_dir=None, merge_no_span_structure=True, table_char_dict_path=None, layout_model_dir=None, layout_dict_path=None, layout_score_threshold=0.5, layout_nms_threshold=0.5, kie_algorithm='LayoutXLM', ser_model_dir=None, re_model_dir=None, use_visual_backbone=True, ser_dict_path='../train_data/XFUND/class_list_xfun.txt', ocr_order_method=None, mode='structure', image_orientation=False, layout=True, table=True, ocr=True, recovery=False, use_pdf2docx_api=False, lang='ch', det=True, rec=True, type='ocr', ocr_version='PP-OCRv3', structure_version='PP-StructureV2')
  [2023/03/16 11:34:22] ppocr DEBUG: dt_boxes num : 3, elapse : 0.06923604011535645
  [2023/03/16 11:34:22] ppocr DEBUG: cls num  : 3, elapse : 0.019355058670043945
  [2023/03/16 11:34:24] ppocr DEBUG: rec_res num  : 3, elapse : 1.6617558002471924
  [[[12.0, 28.0], [254.0, 28.0], [254.0, 41.0], [12.0, 41.0]], ('时，一定要注意不能包裹while语句', 0.8965110778808594)]
  [[[11.0, 109.0], [32.0, 109.0], [32.0, 126.0], [11.0, 126.0]], ('例：', 0.9490082263946533)]
  时，一定要注意不能包裹while语句
  例：

注: 第一次使用时会下载一些包. 比如我的下载到了用户目录下的 ``.paddleocr`` 位置::

  yanque@yanquedembp docker % ls -lh ~/.paddleocr/whl/*
  /Users/yanque/.paddleocr/whl/cls:
  total 0
  drwxr-xr-x@ 5 yanque  staff   160B  3 16 11:30 ch_ppocr_mobile_v2.0_cls_infer

  /Users/yanque/.paddleocr/whl/det:
  total 0
  drwxr-xr-x@ 3 yanque  staff    96B  3 16 11:30 ch

  /Users/yanque/.paddleocr/whl/rec:
  total 0
  drwxr-xr-x@ 3 yanque  staff    96B  3 16 11:30 ch
