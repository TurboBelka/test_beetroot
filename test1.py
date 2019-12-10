
def manage_sqrt_task(value):
    result = app.send_task('tasks.square_root', args=(value,))
    print(result.ready())
    print(result.ready(111))
    print(result.get(timeout=2))


