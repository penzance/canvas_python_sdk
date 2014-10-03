"""
if you ran the generate_sdk_methods.py script you will need to
replace the coresponding methods in courses.py with these. You need
to also check to see if there were any other changes, it may not be a simple
cut and paste.
"""



def create_content_migration_accounts(request_ctx, account_id, migration_type, 
    pre_attachment_name, settings_file_url, 
    pre_attachment_size=None, pre_attachment_content_type=None, 
    pre_attachment_parent_folder_id=None, pre_attachment_parent_folder_path=None,
    pre_attachment_folder=None, pre_attachment_on_duplicate=None,
    settings_source_course_id=None, settings_folder_id=None, 
    settings_overwrite_quizzes=None, settings_question_bank_id=None, 
    settings_question_bank_name=None, date_shift_options_shift_dates=None, 
    date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, 
    date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, 
    date_shift_options_day_substitutions_X=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. `ContentMigrationsController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb>`_ the ContentMigration
    4. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment_size: (optional) The size of the file, in bytes. This field is recommended, as it will let you find out if there's a quota issue before uploading the raw file.
        :type pre_attachment_size: string or None
        :param pre_attachment_content_type: (optional) The content type of the file. If not given, it will be guessed based on the file extension.
        :type pre_attachment_content_type: string or None
        :param pre_attachment_parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_id: string or None
        :param pre_attachment_parent_folder_path: (optional) The path of the folder to store the file in. The path separator is the forward slash `/`, never a back slash. The folder will be created if it does not already exist. This parameter only applies to file uploads in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_path: string or None
        :param pre_attachment_folder: (optional) [deprecated] Use parent_folder_path instead.
        :type pre_attachment_folder: string or None
        :param pre_attachment_on_duplicate: (optional) How to handle duplicate filenames. If `overwrite`, then this file upload will overwrite any other file in the folder with the same name. If `rename`, then this file will be renamed if another file in the folder exists with the given name. If no parameter is given, the default is `overwrite`. This doesn't apply to file uploads in a context that doesn't have folders.
        :type pre_attachment_on_duplicate: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions_X: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions_X: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/accounts/{account_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[size]' : pre_attachment_size,
        'pre_attachment[content_type]' : pre_attachment_content_type,
        'pre_attachment[parent_folder_id]' : pre_attachment_parent_folder_id,
        'pre_attachment[folder]' : pre_attachment_folder,
        'pre_attachment[parent_folder_path]' : pre_attachment_parent_folder_path,
        'pre_attachment[on_duplicate]' : pre_attachment_on_duplicate,
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions_X,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_content_migration_courses(request_ctx, course_id, migration_type, 
    pre_attachment_name, settings_file_url, 
    pre_attachment_size=None, pre_attachment_content_type=None, 
    pre_attachment_parent_folder_id=None, pre_attachment_parent_folder_path=None,
    pre_attachment_folder=None, pre_attachment_on_duplicate=None,
    settings_source_course_id=None, settings_folder_id=None, 
    settings_overwrite_quizzes=None, settings_question_bank_id=None, 
    settings_question_bank_name=None, date_shift_options_shift_dates=None, 
    date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, 
    date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, 
    date_shift_options_day_substitutions_X=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. `ContentMigrationsController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb>`_ the ContentMigration
    4. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment_size: (optional) The size of the file, in bytes. This field is recommended, as it will let you find out if there's a quota issue before uploading the raw file.
        :type pre_attachment_size: string or None
        :param pre_attachment_content_type: (optional) The content type of the file. If not given, it will be guessed based on the file extension.
        :type pre_attachment_content_type: string or None
        :param pre_attachment_parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_id: string or None
        :param pre_attachment_parent_folder_path: (optional) The path of the folder to store the file in. The path separator is the forward slash `/`, never a back slash. The folder will be created if it does not already exist. This parameter only applies to file uploads in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_path: string or None
        :param pre_attachment_folder: (optional) [deprecated] Use parent_folder_path instead.
        :type pre_attachment_folder: string or None
        :param pre_attachment_on_duplicate: (optional) How to handle duplicate filenames. If `overwrite`, then this file upload will overwrite any other file in the folder with the same name. If `rename`, then this file will be renamed if another file in the folder exists with the given name. If no parameter is given, the default is `overwrite`. This doesn't apply to file uploads in a context that doesn't have folders.
        :type pre_attachment_on_duplicate: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions_X: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions_X: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/courses/{course_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[size]' : pre_attachment_size,
        'pre_attachment[content_type]' : pre_attachment_content_type,
        'pre_attachment[parent_folder_id]' : pre_attachment_parent_folder_id,
        'pre_attachment[folder]' : pre_attachment_folder,
        'pre_attachment[parent_folder_path]' : pre_attachment_parent_folder_path,
        'pre_attachment[on_duplicate]' : pre_attachment_on_duplicate,
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions_X,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_content_migration_groups(request_ctx, group_id, migration_type, 
    pre_attachment_name, settings_file_url, 
    pre_attachment_size=None, pre_attachment_content_type=None, 
    pre_attachment_parent_folder_id=None, pre_attachment_parent_folder_path=None,
    pre_attachment_folder=None, pre_attachment_on_duplicate=None, 
    settings_source_course_id=None, settings_folder_id=None, 
    settings_overwrite_quizzes=None, settings_question_bank_id=None, 
    settings_question_bank_name=None, date_shift_options_shift_dates=None, 
    date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, 
    date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, 
    date_shift_options_day_substitutions_X=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. `ContentMigrationsController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb>`_ the ContentMigration
    4. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment_size: (optional) The size of the file, in bytes. This field is recommended, as it will let you find out if there's a quota issue before uploading the raw file.
        :type pre_attachment_size: string or None
        :param pre_attachment_content_type: (optional) The content type of the file. If not given, it will be guessed based on the file extension.
        :type pre_attachment_content_type: string or None
        :param pre_attachment_parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_id: string or None
        :param pre_attachment_parent_folder_path: (optional) The path of the folder to store the file in. The path separator is the forward slash `/`, never a back slash. The folder will be created if it does not already exist. This parameter only applies to file uploads in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_path: string or None
        :param pre_attachment_folder: (optional) [deprecated] Use parent_folder_path instead.
        :type pre_attachment_folder: string or None
        :param pre_attachment_on_duplicate: (optional) How to handle duplicate filenames. If `overwrite`, then this file upload will overwrite any other file in the folder with the same name. If `rename`, then this file will be renamed if another file in the folder exists with the given name. If no parameter is given, the default is `overwrite`. This doesn't apply to file uploads in a context that doesn't have folders.
        :type pre_attachment_on_duplicate: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions_X: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions_X: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/groups/{group_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[size]' : pre_attachment_size,
        'pre_attachment[content_type]' : pre_attachment_content_type,
        'pre_attachment[parent_folder_id]' : pre_attachment_parent_folder_id,
        'pre_attachment[folder]' : pre_attachment_folder,
        'pre_attachment[parent_folder_path]' : pre_attachment_parent_folder_path,
        'pre_attachment[on_duplicate]' : pre_attachment_on_duplicate,
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions_X,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_content_migration_users(request_ctx, user_id, migration_type, 
    pre_attachment_name, settings_file_url, 
    pre_attachment_size=None, pre_attachment_content_type=None, 
    pre_attachment_parent_folder_id=None, pre_attachment_parent_folder_path=None,
    pre_attachment_folder=None, pre_attachment_on_duplicate=None, 
    settings_source_course_id=None, settings_folder_id=None, 
    settings_overwrite_quizzes=None, settings_question_bank_id=None, 
    settings_question_bank_name=None, date_shift_options_shift_dates=None, 
    date_shift_options_old_start_date=None, date_shift_options_old_end_date=None, 
    date_shift_options_new_start_date=None, date_shift_options_new_end_date=None, 
    date_shift_options_day_substitutions_X=None, **request_kwargs):
    """
    Create a content migration. If the migration requires a file to be uploaded
    the actual processing of the file will start once the file upload process is completed.
    File uploading works as described in the {file:file_uploads.html File Upload Documentation}
    except that the values are set on a *pre_attachment* sub-hash.
    
    For migrations that don't require a file to be uploaded, like course copy, the
    processing will begin as soon as the migration is created.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the migration. The migration's progress is linked to with the
    _progress_url_ value.
    
    The two general workflows are:
    
    If no file upload is needed:
    
    1. POST to create
    2. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
    For file uploading:
    
    1. POST to create with file info in *pre_attachment*
    2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
    3. `ContentMigrationsController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb>`_ the ContentMigration
    4. Use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ specified in _progress_url_ to monitor progress
    
     (required if doing .zip file upload)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param migration_type: (required) The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        :type migration_type: string
        :param pre_attachment_name: (required) Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        :type pre_attachment_name: string
        :param settings_file_url: (required) (optional) A URL to download the file from. Must not require authentication.
        :type settings_file_url: string
        :param pre_attachment_size: (optional) The size of the file, in bytes. This field is recommended, as it will let you find out if there's a quota issue before uploading the raw file.
        :type pre_attachment_size: string or None
        :param pre_attachment_content_type: (optional) The content type of the file. If not given, it will be guessed based on the file extension.
        :type pre_attachment_content_type: string or None
        :param pre_attachment_parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_id: string or None
        :param pre_attachment_parent_folder_path: (optional) The path of the folder to store the file in. The path separator is the forward slash `/`, never a back slash. The folder will be created if it does not already exist. This parameter only applies to file uploads in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type pre_attachment_parent_folder_path: string or None
        :param pre_attachment_folder: (optional) [deprecated] Use parent_folder_path instead.
        :type pre_attachment_folder: string or None
        :param pre_attachment_on_duplicate: (optional) How to handle duplicate filenames. If `overwrite`, then this file upload will overwrite any other file in the folder with the same name. If `rename`, then this file will be renamed if another file in the folder exists with the given name. If no parameter is given, the default is `overwrite`. This doesn't apply to file uploads in a context that doesn't have folders.
        :type pre_attachment_on_duplicate: string or None
        :param settings_source_course_id: (optional) The course to copy from for a course copy migration. (required if doing course copy)
        :type settings_source_course_id: string or None
        :param settings_folder_id: (optional) The folder to unzip the .zip file into for a zip_file_import.
        :type settings_folder_id: string or None
        :param settings_overwrite_quizzes: (optional) Whether to overwrite quizzes with the same identifiers between content packages.
        :type settings_overwrite_quizzes: boolean or None
        :param settings_question_bank_id: (optional) The existing question bank ID to import questions into if not specified in the content package.
        :type settings_question_bank_id: integer or None
        :param settings_question_bank_name: (optional) The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        :type settings_question_bank_name: string or None
        :param date_shift_options_shift_dates: (optional) Whether to shift dates
        :type date_shift_options_shift_dates: boolean or None
        :param date_shift_options_old_start_date: (optional) The original start date of the source content/course
        :type date_shift_options_old_start_date: date or None
        :param date_shift_options_old_end_date: (optional) The original end date of the source content/course
        :type date_shift_options_old_end_date: date or None
        :param date_shift_options_new_start_date: (optional) The new start date for the content/course
        :type date_shift_options_new_start_date: date or None
        :param date_shift_options_new_end_date: (optional) The new end date for the source content/course
        :type date_shift_options_new_end_date: date or None
        :param date_shift_options_day_substitutions_X: (optional) Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        :type date_shift_options_day_substitutions_X: integer or None
        :return: Create a content migration
        :rtype: requests.Response (with ContentMigration data)

    """

    path = '/v1/users/{user_id}/content_migrations'
    payload = {
        'migration_type' : migration_type,
        'pre_attachment[name]' : pre_attachment_name,
        'pre_attachment[size]' : pre_attachment_size,
        'pre_attachment[content_type]' : pre_attachment_content_type,
        'pre_attachment[parent_folder_id]' : pre_attachment_parent_folder_id,
        'pre_attachment[folder]' : pre_attachment_folder,
        'pre_attachment[parent_folder_path]' : pre_attachment_parent_folder_path,
        'pre_attachment[on_duplicate]' : pre_attachment_on_duplicate,
        'settings[file_url]' : settings_file_url,
        'settings[source_course_id]' : settings_source_course_id,
        'settings[folder_id]' : settings_folder_id,
        'settings[overwrite_quizzes]' : settings_overwrite_quizzes,
        'settings[question_bank_id]' : settings_question_bank_id,
        'settings[question_bank_name]' : settings_question_bank_name,
        'date_shift_options[shift_dates]' : date_shift_options_shift_dates,
        'date_shift_options[old_start_date]' : date_shift_options_old_start_date,
        'date_shift_options[old_end_date]' : date_shift_options_old_end_date,
        'date_shift_options[new_start_date]' : date_shift_options_new_start_date,
        'date_shift_options[new_end_date]' : date_shift_options_new_end_date,
        'date_shift_options[day_substitutions][X]' : date_shift_options_day_substitutions_X,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


