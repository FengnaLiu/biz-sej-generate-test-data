import sys
import json
from google.cloud import pubsub_v1

if __name__ == '__main__':
    data={}
    data["id"]="20201130000000"
    data["sendtimes"]=1
    data['total']=30000
    data["timestamp"]="20201130000000"
    entry_list=[]
    for i in range(6000):
        entry={}
        entry["store_cd"]="000001"
        entry["today_date_yyyymmdd"]="20201130"
        entry["barcode"]="1111111111111"
        entry["item_name"]="name_"+"{:_>17}".format(i)
        entry["sales_report_type"]="1"
        entry["link_content_flag"]="1"
        entry["freshness_manegement_type"]='1'
        entry["out_of_freshness_time_type"]="1"
        entry["delivery_freshness"]="123"
        entry["sales_freshness"]="123"
        entry["freshness_date_type"]="1"
        entry["in_store_item_totaling_flag"]="1"
        entry["sales_stop_flag"]="1"
        entry["payment_status_1"]="0123456789"
        entry["unit_price_today"]=1234567
        entry["tax_type_today"]="1"
        entry["tax_rate_today"]="123"
        entry["store_promotion_number_today"]="00"
        entry["store_price_up_down_today"]=12345
        entry["promotion_number_1_today"]='123'
        entry["promotion_number_2_today"]='123'
        entry["promotion_number_3_today"]='123'
        entry["promotion_category_1_today"]='12'
        entry["promotion_category_2_today"]='12'
        entry["promotion_category_3_today"]='12'
        entry["unit_price_next_day"]=1234567
        entry["tax_type_next_day"]="1"
        entry["tax_rate_next_day"]="123"
        entry["store_promotion_number_next_day"]='12'
        entry["store_price_up_down_next_day"]=12345
        entry["promotion_number_1_next_day"]="123"
        entry['promotion_number_2_next_day']="123"
        entry['promotion_number_3_next_day']="123"
        entry["promotion_category_1_next_day"]="12"
        entry["promotion_category_2_next_day"]="12"
        entry["promotion_category_3_next_day"]="12"
        entry["subtotal_promotion_target_flag"]="1"
        entry["tax_free_type"]="1"
        entry["promotion_number_4_today"]="123"
        entry["promotion_number_5_today"]="123"
        entry["promotion_category_4_today"]="12"
        entry["promotion_category_5_today"]="12"
        entry["promotion_number_4_next_day"]="123"
        entry["promotion_number_5_next_day"]="123"
        entry["promotion_category_4_next_day"]="12"
        entry["promotion_category_5_next_day"]="12"
        entry["provisional_settlement_prohibition_flag"]="1"
        entry["payment_status_2"]="12"
        entry["plu_create_type"]="1"
        entry_list.append(entry)
    data["item_list"]=entry_list
    print(len(json.dumps(entry_list).encode('utf-8')))
    pub_client = pubsub_v1.PublisherClient()
    topic_path = pub_client.topic_path("sej-dev-spanner-test", "liu-test")
    contents = json.dumps(data)
    contents = contents.encode('utf-8')
    print(len(contents))
    # future = pub_client.publish(topic_path, data=contents)
    # print('Published message ID {}.'.format(future.result()))

    # for j in range(30):
    #     # file="test_"+"{:0>2}".format(j)+".json"
    #     # fw=open(file,'w')
    #     # json.dump(data,fw,indent=4)
    #     pub_client = pubsub_v1.PublisherClient()
    #     topic_path = pub_client.topic_path("sej-dev-spanner-test", "liu-test")
    #     contents = json.dumps(data)
    #     contents = contents.encode('utf-8')
    #     future = pub_client.publish(topic_path, data=contents)
    #     print('Published {} of message ID {}.'.format(contents, future.result()))


