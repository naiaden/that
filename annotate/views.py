from django.shortcuts import render, get_object_or_404
from annotation.models import Tweet, Annotation_eb, Annotation_vl, HUMORTYPES, SOURCE, DISTANCEEB,\
    CONTENTTYPE, FEAR, Student, DISTANCEVL, ATTITUDE
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    all_unannotated = Annotation_vl.objects.filter(is_filled=False)
    
    nr_annotations_vl = Annotation_vl.objects.filter(is_filled=True).count()
    nr_annotations_eb = Annotation_eb.objects.filter(is_filled=True).count()
    nr_annotations = nr_annotations_vl + nr_annotations_eb
    
    nr_tweets_vl = Annotation_vl.objects.filter(is_filled=True).values("tweet_id").distinct().count()
    nr_tweets_eb = Annotation_eb.objects.filter(is_filled=True).values("tweet_id").distinct().count()
    nr_tweets = nr_tweets_vl + nr_tweets_eb
    
    student_info = {}
    for student in Student.objects.all():
        student_info[student] = {}
        student_info[student]['vl'] = len(Annotation_vl.objects.filter(student_id=student.student_id).filter(is_filled=True))
        student_info[student]['eb'] = len(Annotation_eb.objects.filter(student_id=student.student_id).filter(is_filled=True))
    
    context = { 'nr_annotations': nr_annotations,
                'nr_annotations_vl': nr_annotations_vl,
                'nr_annotations_eb': nr_annotations_eb,
                'nr_tweets': nr_tweets,
                'nr_tweets_vl': nr_tweets_vl,
                'nr_tweets_eb': nr_tweets_eb,
                'student_info': student_info }
    return render(request, 'annotate/index.html', context)

def annotations(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)

    # get ebola annotations
    annotations_eb = Annotation_eb.objects.all().filter(student_id=student_id)
    for annotation_eb in annotations_eb:
        tweet = Tweet.objects.all().filter(tweet_id=annotation_eb.tweet_id)
        annotation_eb.tweet_text = tweet.tweet_text

    # get vluchtelingen annotations
    annotations_vl = Annotation_vl.objects.all().filter(student_id=student_id)
    for annotation_vl in annotations_vl:
        tweet = Tweet.objects.all().filter(tweet_id=annotation_vl.tweet_id)
        annotation_vl.tweet_text = tweet.tweet_text

    context = {
        'annotations_eb': annotations_eb,
        'annotations_vl': annotations_vl,
    }

    return render(request, 'annotate/annotations.html', context)


def change_annotation_eb(request, student_id, annotation_id):
    student = get_object_or_404(Student, student_id=student_id)
    annotation = get_object_or_404(Annotation_eb, annotation_id=annotation_id)




def detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    
    remaining_vl = Annotation_vl.objects.filter(student_id=student_id).filter(is_filled=False).count()
    remaining_eb = Annotation_eb.objects.filter(student_id=student_id).filter(is_filled=False).count()
    remaining = remaining_vl + remaining_eb
    
    twannotations = {}

    a_type = ''
    if remaining:      
        #annotations = Annotation_vl.objects.filter(student_id=student_id).filter(is_filled=False).first()
        if remaining_vl:
            annotation = Annotation_vl.objects.filter(student_id=student_id).filter(is_filled=False).first()
            a_type = 'vl'
            tweets = Tweet.objects.filter(tweet_id__in=[x.tweet_id for x in Annotation_vl.objects.filter(student_id=student_id)])
        else:
            annotation = Annotation_eb.objects.filter(student_id=student_id).filter(is_filled=False).first()
            a_type = 'eb'
            tweets = Tweet.objects.filter(tweet_id__in=[x.tweet_id for x in Annotation_eb.objects.filter(student_id=student_id)])
        
        twannotations[annotation.tweet_id] = {}
        twannotations[annotation.tweet_id]['annotation'] = annotation
        for tweet in tweets:
            if tweet.tweet_id == annotation.tweet_id:
                twannotations[tweet.tweet_id]['tweet'] = tweet
                break

    
    return render(request, 'annotation/detail.html', 
                  { 'student': student,
                'type': a_type,
                'humor_types': HUMORTYPES,
                'distance_eb': DISTANCEEB,
                'distance_vl': DISTANCEVL,
                'source': SOURCE,
                'content_type': CONTENTTYPE,
                'fear': FEAR,
                'attitude': ATTITUDE,   
                'twannotations': twannotations,
                #'annotations': kvannotations,
                #'tweets': kvtweets,
                'remaining_vl': remaining_vl,
                'remaining_eb': remaining_eb,
                'remaining': remaining }
                  )


def addannotation(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
   
    annotation_type = request.POST['type']

    if annotation_type == 'vl':
        try:
            for annotation in Annotation_vl.objects.filter(student_id=student_id):
                if str(annotation.annotation_id) == str(request.POST['submit']):
                    selected_annotation = annotation
                    break
        except (KeyError, Annotation_vl.DoesNotExist):
            return render(request, 'annotate/detail.html', {
                'student': student,
                'error_message': "You didn't select a valid annotation",
                })
        else:
            selected_annotation.humor_type = request.POST['humortype']
            selected_annotation.distance = request.POST['distancevl']
            selected_annotation.source = request.POST['source']
            selected_annotation.content_type = request.POST['contenttype']
            selected_annotation.attitude = request.POST['attitude']
            selected_annotation.is_filled = True
            selected_annotation.save()
    else: # 'eb'
        try:
            for annotation in Annotation_eb.objects.filter(student_id=student_id):
                if str(annotation.annotation_id) == str(request.POST['submit']):
                    selected_annotation = annotation
                    break
        except (KeyError, Annotation_eb.DoesNotExist):
            return render(request, 'annotate/detail.html', {
                'student': student,
                'error_message': "You didn't select a valid annotation",
                })
        else:
            selected_annotation.humor_type = request.POST['humortype']
            selected_annotation.distance = request.POST['distanceeb']
            selected_annotation.source = request.POST['source']
            selected_annotation.content_type = request.POST['contenttype']
            selected_annotation.fear = request.POST['fear']
            selected_annotation.is_filled = True
            selected_annotation.save()

        
    
    remaining_vl = Annotation_vl.objects.filter(student_id=student_id).filter(is_filled=False).count()
    remaining_eb = Annotation_eb.objects.filter(student_id=student_id).filter(is_filled=False).count()
    remaining = remaining_vl + remaining_eb
    
    twannotations = {}
    
    a_type = ''
    if remaining:      
        #annotations = Annotation_vl.objects.filter(student_id=student_id).filter(is_filled=False).first()
        if remaining_vl:
            annotation = Annotation_vl.objects.filter(student_id=student_id).filter(is_filled=False).first()
            a_type = "vl"
            tweets = Tweet.objects.filter(tweet_id__in=[x.tweet_id for x in Annotation_vl.objects.filter(student_id=student_id)])
        else:
            annotation = Annotation_eb.objects.filter(student_id=student_id).filter(is_filled=False).first()
            a_type = "eb"
            tweets = Tweet.objects.filter(tweet_id__in=[x.tweet_id for x in Annotation_eb.objects.filter(student_id=student_id)])
        
        twannotations[annotation.tweet_id] = {}
        twannotations[annotation.tweet_id]['annotation'] = annotation
        for tweet in tweets:
            if tweet.tweet_id == annotation.tweet_id:
                twannotations[tweet.tweet_id]['tweet'] = tweet
                break
    
    
    return render(request, 'annotation/detail.html', 
        { 'student': student,
         'type': a_type,
        'humor_types': HUMORTYPES,
        'distance_eb': DISTANCEEB,
        'distance_vl': DISTANCEVL,
        'attitude': ATTITUDE,
        'source': SOURCE,
        'content_type': CONTENTTYPE,
        'fear': FEAR,
        'twannotations': twannotations,
        #'annotations': kvannotations,
        #'tweets': kvtweets,
        'remaining_vl': remaining_vl,
        'remaining_eb': remaining_eb,
        'remaining': remaining }
         )
