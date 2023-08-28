from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def new_conversation(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if item.created_by == request.user:
        return redirect("dashboard:index")

    conversations = Conversation.objects.filter(item=item).filter(
        members__in=[request.user.id]
    )

    if conversations:
        return redirect(
            "conversation:details", conversation_id=conversations.first().id
        )  # redirect to conversation

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid:
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)

            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            return redirect("item:details", id=item_id)
    else:
        form = ConversationMessageForm()

    return render(request, "conversations/new.html", {"form": form})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, "conversations/inbox.html", {"conversations": conversations})


@login_required
def details(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid:
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            conversation.save()
            return redirect("conversation:details", conversation_id=conversation_id)
    else:
        form = ConversationMessageForm()

    return render(
        request,
        "conversations/details.html",
        {"conversation": conversation, "form": form},
    )
