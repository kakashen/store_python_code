import json


def save(msg_list):
    msg_list = msg_list.replace("\/", "/")
    data = json.loads(msg_list)
    msg_list = data.get("list")
    for msg in msg_list:
        p_date = msg.get("comm_msg_info").get("datetime")
        msg_info = msg.get("app_msg_ext_info")  # 非图文消息没有此字段
        if msg_info:
            WeiXinCrawler._insert(msg_info, p_date)
            multi_msg_info = msg_info.get("multi_app_msg_item_list")  # 多图文推送，把第二条第三条也保存
            for msg_item in multi_msg_info:
                WeiXinCrawler._insert(msg_item, p_date)
        else:
            logger.warning(u"此消息不是图文推送，data=%s" % json.dumps(msg.get("comm_msg_info")))



def _insert(item, p_date):
    keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
    sub_data = utils.sub_dict(item, keys)
    post = Post(**sub_data)
    p_date = datetime.fromtimestamp(p_date)
    post["p_date"] = p_date
    logger.info('save data %s ' % post.title)
    try:
        post.save()
    except Exception as e:
        logger.error("保存失败 data=%s" % post.to_json(), exc_info=True)