# import asyncio

# async def send_mail():
#     print("sending email...")
#     await asyncio.sleep(20)
#     print("mail sent")
#     return "send mail"

# async def process_payment():
#     print("sending payment...")
#     await asyncio.sleep(10)
#     print("payment sent")
#     return "payment completed successfully"

# async def main():
#     email_task= asyncio.create_task(send_mail())
#     payment_result = await process_payment()
#     print("before main")
#     await email_task
#     print("ehheheheh")
#     print(payment_result)
#     print("after main")

# asyncio.run(main())