from django.shortcuts import render, get_object_or_404
from .models import Tweet

# Create your views here.
def index(request):
    all_tweets = Tweet.objects.all()
    context = { 'all_tweets': all_tweets }
    return render(request, 'annotation/index.html', context)

def detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, tweet_id=tweet_id)
    return render(request, 'annotation/detail.html', { 'tweet': tweet })