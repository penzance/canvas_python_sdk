from canvas_sdk import client, utils

def show_outcome(request_ctx, id, **request_kwargs):
    """
    Returns the details of the outcome with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Show an outcome
        :rtype: requests.Response (with Outcome data)

    """

    path = '/v1/outcomes/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_outcome(request_ctx, id, title=None, display_name=None, description=None, vendor_guid=None, mastery_points=None, ratings_description=None, ratings_points=None, **request_kwargs):
    """
    Modify an existing outcome. Fields not provided are left as is;
    unrecognized fields are ignored.
    
    If any new ratings are provided, the combination of all new ratings
    provided completely replace any existing embedded rubric criterion; it is
    not possible to tweak the ratings of the embedded rubric criterion.
    
    A new embedded rubric criterion's mastery_points default to the maximum
    points in the highest rating if not specified in the mastery_points
    parameter. Any new ratings lacking a description are given a default of "No
    description". Any new ratings lacking a point value are given a default of
    0.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param title: (optional) The new outcome title.
        :type title: string or None
        :param display_name: (optional) A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names.
        :type display_name: string or None
        :param description: (optional) The new outcome description.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param mastery_points: (optional) The new mastery threshold for the embedded rubric criterion.
        :type mastery_points: integer or None
        :param ratings_description: (optional) The description of a new rating level for the embedded rubric criterion.
        :type ratings_description: string or None
        :param ratings_points: (optional) The points corresponding to a new rating level for the embedded rubric criterion.
        :type ratings_points: integer or None
        :return: Update an outcome
        :rtype: requests.Response (with Outcome data)

    """

    path = '/v1/outcomes/{id}'
    payload = {
        'title' : title,
        'display_name' : display_name,
        'description' : description,
        'vendor_guid' : vendor_guid,
        'mastery_points' : mastery_points,
        'ratings[description]' : ratings_description,
        'ratings[points]' : ratings_points,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


