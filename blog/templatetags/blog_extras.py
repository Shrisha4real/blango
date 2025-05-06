from django import template
from django.utils.html import format_html
import pprint
from blog.models import Posts

register = template.Library()

@register.simple_tag
def row(extra_classes=""):
    return format_html(f'<div class="row {extra_classes}">' )


@register.simple_tag
def endrow():
    return format_html("</div>")

@register.simple_tag
def rowChild(extra_classes=""):
    return format_html(f"<div col-auto {extra_classes}>")
@register.simple_tag
def endRowChild():
    return format_html("</div>")

@register.simple_tag(takes_context=True)
def author_details_tag(context):
    print("CONTEXT" , pprint.pformat(context["request"].user))
    request = context["request"]
    current_user = request.user
    post = context["post"]
    author = post.author

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Posts.objects.exclude(pk=post.pk)[:5]
    return {'posts':posts , 'title':"Recents" }

