
def manage_sqrt_task(value):
    result = app.send_task('tasks.square_root', args=(value,))
    print(result.ready())
    print(result.remove())
    print(result.ready(111))
    print("test") 
    print(result.get(timeout=2))


