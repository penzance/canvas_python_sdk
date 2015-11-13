from canvas_sdk.methods import courses, external_tools, modules, assignments
from canvas_sdk import RequestContext
import json
import collections

# Instructor should provide following information
oauth_token = '7~98d8KnPbCj7wnA3GLyHIvh4yxHz7t2U6SPp7OLdvscWSN82qCnZbEWebFJVEb0b3'
canvas_url = 'https://canvas.instructure.com/api'
course_code = "OpenDSA"


# init the request context
request_ctx = RequestContext(oauth_token, canvas_url)

# get course_id
results = courses.list_your_courses(request_ctx, 'total_scores')
for i, course in enumerate(results.json()):
    if course.get("course_code") == course_code:
        course_id = course.get("id")

# Instructor should provide external tool info
external_tool_name = "ltitest"
privacy_level = "public"
consumer_key = "test"
shared_secret = "secret"
config_type = "by_url"
config_url = "https://ltitest.cs.vt.edu:9292//tool_config.xml"


# configure the course external_tool
results = external_tools.create_external_tool_courses(
    request_ctx, course_id, external_tool_name, privacy_level=privacy_level,
    consumer_key=consumer_key, shared_secret=shared_secret,
    config_type=config_type, config_url=config_url)


with open('CS3114.json') as data_file:
    config_data = json.load(
        data_file, object_pairs_hook=collections.OrderedDict)

# update the course name
course_name = config_data.get("title")
results = courses.update_course(
    request_ctx, course_id, course_name=course_name)

chapters = config_data.get("chapters")

for chapter in chapters:
    chapter_obj = chapters[str(chapter)]
    # OpenDSA chapters will map to canvas modules
    results = modules.create_module(
        request_ctx, course_id, str(chapter) + " Chapter")
    module_id = results.json().get("id")
    for module in chapter_obj:
        module_obj = chapter_obj[str(module)]
        module_name = module_obj.get("long_name")
        # OpenDSA module header will map to canvas text header
        results = modules.create_module_item(
            request_ctx, course_id, module_id, 'SubHeader',
            module_item_content_id=None,
            module_item_title=module_name + " Module",
            module_item_indent=0)
        item_id = results.json().get("id")
        exercises = module_obj.get("exercises")
        if bool(exercises):
            exercise_counter = 1
            for exercise in exercises:
                exercise_obj = exercises[str(exercise)]
                long_name = exercise_obj.get("long_name")
                points = exercise_obj.get("points", 0)
                if long_name:
                    print(str(exercise_counter).zfill(2)) + \
                        " " + long_name
                    # OpenDSA exercises will map to canvas assignments
                    results = assignments.create_assignment(
                        request_ctx, course_id,
                        long_name,
                        assignment_submission_types="external_tool",
                        assignment_external_tool_tag_attributes={
                            "url": "https://ltitest.cs.vt.edu:9292/lti_tool?problem_type=module&problem_url=CS3114/html/&short_name=" + module_name + "-" + str(exercise_counter).zfill(2)},
                        assignment_points_possible=points,
                        assignment_description=long_name)
                    assignment_id = results.json().get("id")

                    # add assignment to module
                    results = modules.create_module_item(
                        request_ctx, course_id, module_id,
                        'Assignment', module_item_content_id=assignment_id,
                        module_item_indent=1)
                    exercise_counter += 1
        else:
            results = modules.create_module_item(
                request_ctx, course_id, module_id,
                'ExternalTool',
                module_item_external_url="https://ltitest.cs.vt.edu:9292/lti_tool?problem_type=module&problem_url=CS3114/html/&short_name=" +
                module_name + "-00",
                module_item_content_id=None,
                module_item_title=module_name + " Module",
                module_item_indent=1)

    # publish the module
    results = modules.update_module(
        request_ctx, course_id, module_id, module_published=True)
