from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AAAA_mCm21w:APA91bGSUlb9rJ_A8Fi92Jcl_HEYlZduYaflPFq7lyx4akePCnuOdkmcu0ia9Yc0w7FuEtXNx7CMBERA1p-OMnA_2NZ-DPVaEJwhrtlKvdctBYxdEiJm-78-8B4nkXa4UmrjOsvZC45l")
registration_id = None
message_title = "Simo Notification"
def app_notification(message_body):
    result = push_service.notify_topic_subscribers(topic_name="simo-client-android", message_body=message_body)
    print (result)

app_notification("TES FENYMOTION")
