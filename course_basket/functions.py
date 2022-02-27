from home.models import Course
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from users.models import Notification
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
# from home.filters import ProjectFilter
from django.contrib.auth.models import User
from collections import Counter
from django.db.models import Q

# def get_filtered_projects(request, all_projects):
#     myFilter = ProjectFilter(request.GET,queryset=all_projects)
#     filtered_projects= myFilter.qs
#     return filtered_projects

# def get_most_common_tags(size):
#     projects = Project.objects.all()
#     tags = []
#     for project in projects:
#         project_tags = project.Tags.all()
#         for project_tag in project_tags:
#             tags.append(project_tag)
#     return [x for x in Counter(tags)][:size]

# def get_user_projects(user):
#     all_project_list = Course.objects.all().order_by('credits')
#     applied = all_project_list.filter(AlreadyApplied=user.profile.sem)
#     floated = all_project_list.filter(FloatedBy=user)
#     requested = all_project_list.filter(ApplyRequest=user)
#     starred = user.profile.starred_projects.all()
#     return [floated, applied, requested, starred]

def return_sem(course_sem_column):
    switcher = {
        '1st' : 'sem1',
        '2nd' : 'sem2',
        '3rd' : 'sem3',
        '4th' : 'sem4',
        '5th' : 'sem5',
        '6th' : 'sem6',
        '7th' : 'sem7',
        '8th' : 'sem8'
    }

    # return switcher.get(course_sem_column)
    return switcher[course_sem_column]

    # match course_sem_column:
    #     case "1st":
    #         return "sem1"
    #     case "2nd":
    #         return "sem2"
    #     case "3rd":
    #         return "sem3"


# def select_courses():



# def drop_courses():



# def add_courses(user):


def get_user_course(user):  # filters courses available for a particular semester and basket wise
    all_project_list = Course.objects.all()

    sem = user.profile.sem
    sem_col_course = return_sem(sem)
    offered = all_project_list.exclude(**{sem_col_course : "NULL"})
    ic = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "IC Compulsory")
    sci_b1 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 1")
    sci_b2 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 2")
    sci_b3 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 3")
    hss = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "HSS")
    dc = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "DE")
    fe = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "FE")
    mtp = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "")


    compulsary = offered.filter(**{sem_col_course : "C"})
    elective = offered.filter(**{sem_col_course : "E"})

    return [compulsary, elective, ic, sci_b1, sci_b2, sci_b3, hss, dc, fe, mtp]


def get_user_course_id(user):  # filters courses available for a particular semester and basket wise
    all_project_list = Course.objects.all()

    sem = user.profile.sem
    sem_col_course = return_sem(sem)
    offered = all_project_list.exclude(**{sem_col_course : "NULL"})
    ic = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "IC Compulsory")
    sci_b1 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 1")
    sci_b2 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 2")
    sci_b3 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 3")
    hss = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "HSS")
    dc = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "DE")
    fe = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "FE")
    mtp = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "")


    compulsary_id = []
    electives_id = []
    ic_id = []
    sci_b1_id = []
    sci_b2_id = []
    sci_b3_id = []
    hss_id = []
    dc_id = []
    fe_id = []
    mtp_id = []

    compulsary = offered.filter(**{sem_col_course : "C"})
    elective = offered.filter(**{sem_col_course : "E"})

    for course in compulsary:
        compulsary_id.append(course.id)
    for course in elective:
        electives_id.append(course.id)
    for course in ic:
        ic_id.append(course.id)
    for course in sci_b1:
        sci_b1_id.append(course.id)
    for course in sci_b2:
        sci_b2_id.append(course.id)
    for course in sci_b3:
        sci_b3_id.append(course.id)
    for course in hss:
        hss_id.append(course.id)
    for course in dc:
        dc_id.append(course.id)
    for course in fe:
        fe_id.append(course.id)
    for course in mtp:
        mtp_id.append(course.id)

    return [compulsary_id, electives_id, ic_id, sci_b1_id, sci_b2_id, sci_b3_id, hss_id, dc_id, fe_id, mtp_id]





def get_course_sem(sem):  # filters courses available for a particular semester and basket wise
    all_project_list = Course.objects.all()

    # sem = user.profile.sem
    sem_col_course = return_sem(sem)

    offered = all_project_list.exclude(**{sem_col_course : "NULL"})
    ic = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "IC Compulsory")
    sci_b1 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 1")
    sci_b2 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 2")
    sci_b3 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 3")
    hss = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "HSS")
    dc = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "DE")
    fe = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "FE")
    mtp = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "")


    compulsary = offered.filter(**{sem_col_course : "C"})
    elective = offered.filter(**{sem_col_course : "E"})

    return [compulsary, elective, ic, sci_b1, sci_b2, sci_b3, hss, dc, fe, mtp]


def get_course_sem_id(sem):  # filters courses available for a particular semester and basket wise
    all_project_list = Course.objects.all()

    # sem = user.profile.sem
    sem_col_course = return_sem(sem)
    offered = all_project_list.exclude(**{sem_col_course : "NULL"})
    ic = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "IC Compulsory")
    sci_b1 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 1")
    sci_b2 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 2")
    sci_b3 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 3")
    hss = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "HSS")
    dc = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "DE")
    fe = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "FE")
    mtp = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "")


    compulsary_id = []
    electives_id = []
    ic_id = []
    sci_b1_id = []
    sci_b2_id = []
    sci_b3_id = []
    hss_id = []
    dc_id = []
    fe_id = []
    mtp_id = []

    compulsary = offered.filter(**{sem_col_course : "C"})
    elective = offered.filter(**{sem_col_course : "E"})

    for course in compulsary:
        compulsary_id.append(course.id)
    for course in elective:
        electives_id.append(course.id)
    for course in ic:
        ic_id.append(course.id)
    for course in sci_b1:
        sci_b1_id.append(course.id)
    for course in sci_b2:
        sci_b2_id.append(course.id)
    for course in sci_b3:
        sci_b3_id.append(course.id)
    for course in hss:
        hss_id.append(course.id)
    for course in dc:
        dc_id.append(course.id)
    for course in fe:
        fe_id.append(course.id)
    for course in mtp:
        mtp_id.append(course.id)

    return [compulsary_id, electives_id, ic_id, sci_b1_id, sci_b2_id, sci_b3_id, hss_id, dc_id, fe_id, mtp_id]


def do_task(request,course_id, task):
    # course_id = request.GET.get('course_id')
    course = Course.objects.get(id=course_id)
    current_user = request.user
    # if task == "Apply":
    #     apply_on_project(request, project)
    # elif task == "Withdraw":
    #     withdraw_from_project(request,project)
    # elif task == "Leave":
    #     leave_project(request, project)
    if task == "Add":
        current_user.profile.completed_courses.add(course)
    elif task == "drop":
        current_user.profile.current_courses.remove(course)
    elif task == "Submit":   
        current_user.profile.current_courses.add(course)
    elif task == "update_tot_credits":
        tot = 0
        for i in current_user.profile.completed_courses.all():
            tot = tot + i.credits
        for i in current_user.profile.current_courses.all():
            tot = tot + i.credits
        current_user.profile.total_credits = tot

def update_visible_courses(request):
    current_user = request.user
    all_project_list = Course.objects.all()

    # user_courses_sem = get_user_course(request.user)
    # print(user_courses_sem)

    user_courses_completed = current_user.profile.completed_courses.all()
    user_courses_current = current_user.profile.current_courses.all()

    # # sem = user.profile.sem
    sem = request.user.profile.sem

    sem_col_course = return_sem(sem)
    offered = all_project_list.exclude(**{sem_col_course : "NULL"})
    ic = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "IC Compulsory")
    sci_b1 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 1")
    sci_b2 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 2")
    sci_b3 = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "Science Basket 3")
    hss = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "HSS")
    dc = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "DE")
    fe = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "FE")
    mtp = all_project_list.exclude(**{sem_col_course : "NULL"}).filter(type = "")

    compulsary = offered.filter(**{sem_col_course : "C"})
    elective = offered.filter(**{sem_col_course : "E"})
    new_sem_courses = []

    for course in user_courses_completed:
        ic = ic.exclude(id = course.id)
        sci_b1 = sci_b1.exclude(id = course.id)
        sci_b2 = sci_b2.exclude(id = course.id)
        sci_b3 = sci_b3.exclude(id = course.id)
        hss = hss.exclude(id = course.id)
        dc = dc.exclude(id = course.id)
        fe = fe.exclude(id = course.id)
        mtp = mtp.exclude(id = course.id)
        compulsary = compulsary.exclude(id = course.id)
        elective = elective.exclude(id = course.id)

    for course in user_courses_current:
        ic = ic.exclude(id = course.id)
        sci_b1 = sci_b1.exclude(id = course.id)
        sci_b2 = sci_b2.exclude(id = course.id)
        sci_b3 = sci_b3.exclude(id = course.id)
        hss = hss.exclude(id = course.id)
        dc = dc.exclude(id = course.id)
        fe = fe.exclude(id = course.id)
        mtp = mtp.exclude(id = course.id)
        compulsary = compulsary.exclude(id = course.id)
        elective = elective.exclude(id = course.id)

    
    # for course in user_courses_completed:
    #     print(course)
    #     for type in user_courses_sem:
    #         print(type)
    #         type = type.exclude(id = course.id)
    #         print(type)

    
    
    # for course in user_courses_current:
    #     # offered = all_project_list.exclude(id = course.id)
    #     # print(course)
    #     for type in user_courses_sem:
    #         # print("before: ",type)
    #         type = type.exclude(id = course.id)
            # print("after: ",type)

    # return[ic, sci_b1, sci_b2, sci_b3, hss, dc, fe, mtp]
    # return user_courses_sem
    return [compulsary, elective, ic, sci_b1, sci_b2, sci_b3, hss, dc, fe, mtp]

        
    # elif task == "Unlike":
    #     current_user.profile.liked_projects.remove(project)
    #     project.Likes -= 1
    #     project.save()
    # elif task == "Accept" or task == "Reject":
    #     request_user_name = request.GET.get('request_user')
    #     request_user = User.objects.filter(username = request_user_name).first()

    #     project.ApplyRequest.remove(request_user)
    #     if task == "Apply":
    #         project.AlreadyApplied.add(request_user)
