from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from groups.forms import GroupForm
from groups.models import Group

User = get_user_model()

# Create your views here.
class GroupListView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'groups/group_list.html'

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/group_detail.html'

@login_required
def join_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    
    if group:
        group.members.add(User.objects.get(id=request.user.id))

    return redirect('groups:group_detail', slug=slug)

@login_required
def leave_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    
    if group:
        group.members.remove(User.objects.get(id=request.user.id))
        
    return redirect('groups:group_detail', slug=slug)