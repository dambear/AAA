from django.shortcuts import render, redirect
from main.models import Training_Webinars_Table


def tmd(request):
    return render(request, "4_tmd/index.html")

def add_data_tmd(request):
    if request.method == "POST":
        # Get the form data from POST request
        province = request.POST.get("province")
        course_name = request.POST.get("course_name")
        training_track = request.POST.get("training_track")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        time = request.POST.get("time")
        total_num_hours = request.POST.get("total_num_hours")
        nga_m = request.POST.get("nga_m")
        nga_f = request.POST.get("nga_f")
        suc_m = request.POST.get("suc_m")
        suc_f = request.POST.get("suc_f")
        lgu_m = request.POST.get("lgu_m")
        lgu_f = request.POST.get("lgu_f")
        others_m = request.POST.get("others_m")
        others_f = request.POST.get("others_f")
        total_m = request.POST.get("total_m")
        total_f = request.POST.get("total_f")
        total_participants = request.POST.get("total_participants")
        participants_list = request.POST.get("participants_list")
        attendance_sheet = request.POST.get("attendance_sheet")
        group_photo = request.POST.get("group_photo")
        implementation_mode = request.POST.get("implementation_mode")
        certificates_issued = request.POST.get("certificates_issued")
        resource_persons = request.POST.get("resource_persons")
        resource_persons_cv = request.POST.get("resource_persons_cv")
        course_officers = request.POST.get("course_officers")
        course_officers_email = request.POST.get("course_officers_email")
        remarks = request.POST.get("remarks")

        # Create a new instance with the form data
        new_training_webinars =  Training_Webinars_Table(
            province=province,
            course_name=course_name,
            training_track=training_track,
            start_date=start_date,
            end_date=end_date,
            time=time,
            total_num_hours=total_num_hours,
            nga_m=nga_m,
            nga_f=nga_f,
            suc_m=suc_m,
            suc_f=suc_f,
            lgu_m=lgu_m,
            lgu_f=lgu_f,
            others_m=others_m,
            others_f=others_f,
            total_m=total_m,
            total_f=total_f,
            total_participants=total_participants,
            participants_list=participants_list,
            attendance_sheet=attendance_sheet,
            group_photo=group_photo,
            implementation_mode=implementation_mode,
            certificates_issued=certificates_issued,
            resource_persons=resource_persons,
            resource_persons_cv=resource_persons_cv,
            course_officers=course_officers,
            course_officers_email=course_officers_email,
            remarks=remarks
        )

        # Save the new instance
        new_training_webinars.save()

        # Redirect to a specific page
        return redirect("tmd_training_webinars")
    else:
        # Render the form page if the request method is not POST
          return render(request, "4_tmd/add_data_tmd.html")

