from django.shortcuts import render

from LinkedList import LinkedList

linkedlist = LinkedList()


def index(request):
    return render(
        request,
        "linkedlist_app/index.html",
        {"linkedlist": linkedlist, "nodeList": linkedlist.get_values_and_ref()},
    )


def node_action(request):

    data = request.POST["linkedlist_input"]
    operation = request.POST["linkedlist_operation"]

    if operation == "insert" and data != "":
        linkedlist.insert(data)
    elif operation == "remove_first" and linkedlist._len > 0:
        linkedlist.removeFirst()
    elif operation == "append" and data != "":
        linkedlist.append(data)

    return render(
        request,
        "linkedlist_app/index.html",
        {"linkedlist": linkedlist, "nodeList": linkedlist.get_values_and_ref()},
    )
