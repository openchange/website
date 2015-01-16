Mapistore HTTP REST API
=======================

This documentation is work in progress.

.. toctree::
   :maxdepth: 2

Authentication
--------------

TBD

Backend info
------------
.. http:get:: /info/

   Backend information: name, version, implemented capabilities...

   **Example request**:

   .. sourcecode:: http

      GET /info/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "name": "My MAPISTORE Backend",
        "version": 3,
        "capabilities": {
          "soft_delete": true,
          "...": "...",
        },
      },

   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: Ok


Folders
-------

.. http:post:: /folders/

   :synopsis: Creates a new folder and returns its ID.
              ``parent_id`` and ``PidTagDisplayName``` are required.
              Other folder attributes are optional.

   **Example request**:

   .. sourcecode:: http

      POST /folders/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "c7e77cc9999908ec54ae32f1faf17e0e",
        "PidTagDisplayName": "new folder name",
        "PidTagComment": "Comment about the folder"
      }

   :<json string parent_id: Parent Folder Identifier
   :<json string PidTagDisplayName: Name of the folder to create
   :<json string PidTagComment: Comment associated to the folder


   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "68b329da9893e34099c7d8ad5cb9c940"
      }

   :>json string id: Folder Identifier of the folder created
   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 422: The request was well-formed but was unable to be followed due to semantic errors


.. http:get:: /folders/(id)/

   :synopsis: Get all properties of the folder object identified by `id`

   **Example request**:

   .. sourcecode:: http

      GET /folders/c7e77cc9999908ec54ae32f1faf17e0e/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "c7e77cc9999908ec54ae32f1faf17e0e",
        "item_count": 37,
        "PidTagDisplayName": "MyFolderName",
        "PidTagComment": "This is a sample folder"
      },

   :>json string id: Folder identifier

   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


.. http:put:: /folders/(id)/

   :synopsis: Set properties on the folder object identified by `id`

   **Example request**:

   .. sourcecode:: http

      PUT /folders/c7e77cc9999908ec54ae32f1faf17e0e/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
         "PidTagDisplayName": "UpdatedFolderName"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: The update was successfully applied
   :statuscode 400: Bad Request


.. http:head:: /folders/(id)/

   :synopsis: Check if the folder exists

   **Example request**:

   .. sourcecode:: http

      HEAD /folders/c7e77cc9999908ec54ae32f1faf17e0e/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


.. http:delete:: /folders/(id)/

   :synopsis: Recursively delete the folder

   **Example request**:

   .. sourcecode:: http

      DELETE /folders/c7e77cc9999908ec54ae32f1faf17e0e/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No content

   :reqheader Authorization: auth token
   :statuscode 204: Ok
   :statuscode 404: Folder does not exist


.. http:head:: /folders/(id)/messages

   :synopsis: Retrieve the count of messages within specified folder

   **Example request**:

   .. sourcecode:: http

      HEAD /folders/c7e77cc9999908ec54ae32f1faf17e0e/messages HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      X-mapistore-rowcount: 32

   :reqheader Authorization: auth token
   :resheader X-mapistore-rowcount: The number of specified items within the folder
   :statuscode 200: Ok


.. http:head:: /folders/(id)/folders

   :synopsis: Retrieve the count of folders within specified folder

   **Example request**:

   .. sourcecode:: http

      HEAD /folders/c7e77cc9999908ec54ae32f1faf17e0e/folders HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      X-mapistore-rowcount: 2

   :reqheader Authorization: auth token
   :resheader X-mapistore-rowcount: The number of specified items within the folder
   :statuscode 200: Ok


.. http:get:: /folders/(id)/messages

   :synopsis: List of messages within specified folder

   **Example request**:

   .. sourcecode:: http

      GET /folders/c7e77cc9999908ec54ae32f1faf17e0e/messages?properties=id,type HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": "7be92d92557702c8eb2e764266119346",
          "collection": "mails",
        },
        {
          "id": "fa21ee2b607ac6e327ecb39021be5469",
          "collection": "calendars",
        },
        ...
      ]

   :>jsonarr string id: Message identifier
   :>jsonarr string collection: Collection the message belongs to

   :query properties: Comma separated list of properties to return
                      for every folder. If not set all properties will
                      be returned. E.g: ``id,type``
   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


.. http:get:: /folders/(id)/folders

   :synopsis: List of folders within specified folder

   **Example request**:

   .. sourcecode:: http

      GET /folders/c7e77cc9999908ec54ae32f1faf17e0e/folders HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": "7be92d92557702c8eb2e764266119346",
          "collection": "folders",
        },
        {
          "id": "fa21ee2b607ac6e327ecb39021be5469",
          "collection": "folders",
        },
        ...
      ]

   :>jsonarr string id: Folder identifier
   :>jsonarr string type: Collection of the folder

   :query properties: Comma separated list of properties to return
                      for every folder. If not set all properties will
                      be returned. E.g: ``id,type``
   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


.. http:post:: /folders/(id)/empty

   :synopsis: Empty folder identified by `id`

   **Example request**:

   .. sourcecode:: http

      POST /folders/c7e77cc9999908ec54ae32f1faf17e0e/empty HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok


.. http:post:: /folders/(id)/deletemessages

   :synopsis: Delete messages within folder identified by `id`

   **Example request**:

   .. sourcecode:: http

      POST /folders/c7e77cc9999908ec54ae32f1faf17e0e/deletemessages HTTP/1.1
      Host: example.com
      Accept: application/json

      [
         {
            "id": "7be92d92557702c8eb2e764266119346",
         },
         {
            "id": "fa21ee2b607ac6e327ecb39021be5469",
         },
         ...
      ]

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok


Mail
------

.. http:post:: /mails/

   :synopsis: Create a new mail item and return its ID

   **Example request**:

   .. sourcecode:: http

      POST /mails/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "7ac34cce50903fe1e306ab0ede13bcf6e2ebc8e3",
        "PidTagSubject": "My sample mail",
        "PidTagBody": "Sample body"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "51c3187152d0a0daa5e0de4d6e3132cb561135e7"
      }

      :>json string id: Message identifier of the mail item created
      :reqheader Authorization: auth token
      :statuscode 200: Ok


.. http:get:: /mails/(id)/

   :synopsis: Retrieve all the properties of the mail entry
              identified by `id`

   **Example request**:

   .. sourcecode:: http

      GET /mails/51c3187152d0a0daa5e0de4d6e3132cb561135e7/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "51c3187152d0a0daa5e0de4d6e3132cb561135e7",
        "parent_id": "7ac34cce50903fe1e306ab0ede13bcf6e2ebc8e3"
        "PidTagSubject": "My sample mail",
        "PidTagBody": "Sample body"
      },

   :reqheader Authorization: auth token
   :reqheader Accept: the response content depends on on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of the request
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:put:: /mails/(id)/

   :synopsis: Set properties on the mail item object identified by `id`

   **Example request**:

   .. sourcecode:: http

      PUT /mails/51c3187152d0a0daa5e0de4d6e3132cb561135e7/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "PidTagBody": "Sample body v2"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: The update was successfully applied
   :statuscode 400: Bad request


.. http:head:: /mails/(id)/

   :synopsis: Check if the mail item identified by `id` exists

   **Example request**:

   .. sourcecode:: http

      HEAD /mails/51c3187152d0a0daa5e0de4d6e3132cb561135e7/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:delete:: /mails/(id)/

   :synopsis: Delete the mail entry identified by `id`

   **Example request**:

   .. sourcecode:: http

      DELETE /mails/51c3187152d0a0daa5e0de4d6e3132cb561135e7/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No content

   :reqheader Authorization: auth token
   :statuscode 204: Ok
   :statuscode 404: Item does not exist

.. http:head:: /mails/(id)/attachments

   :synopsis: Retrieve the count of attachments within specified mail

   **Example request**:

   .. sourcecode:: http

      HEAD /mails/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      X-mapistore-rowcount: 2

   :reqheader Authorization: auth token
   :resheader X-mapistore-rowcount: The number of specified items within the mail
   :statuscode 200: Ok


.. http:get:: /mails/(id)/attachments

   :synopsis: List of attachments within specified mail

   **Example request**:

   .. sourcecode:: http

      GET /mails/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments?properties=id,PidTagAttachFilename HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": "2cc32afdcba1491d704d02c2eeda57ae3a9bd35e",
          "PidTagAttachFilename": "attach1.foo"
        },
        {
          "id": "d4d6301939fd0d832292c112925a1056a24f8b4e",
          "PidTagAttachFilename": "attach2.foo"
        },
        ...
      ]

   :>jsonarr string id: Attachment identifier
   :>jsonarr string PidTagAttachFilename: Attachment filename

   :query properties: Comma separated list of properties to return
                      for every mail. If not set all properties will
                      be returned. E.g: ``id,PidTagAttachFilename``
   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


Calendar
--------

.. http:post:: /calendars/

   :synopsis: Create a new calendar item and returns its ID

   **Example request**:

   .. sourcecode:: http

      POST /calendars/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "cea793f236334942bdae2c1e6c83607d",
        "PidTagSubject": "My sample appointment",
	"PidTagBody": "Sample body"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "15924213158245d0ad631c6a41a0e7c3"
      }

      :>json string id: Message identifier of the calendar item created
      :reqheader Authorization: auth token
      :statuscode 200: Ok


.. http:get:: /calendars/(id)/

   :synopsis: Retrieve all the properties of the calendar entry
              identified by `id`

   **Example request**:

   .. sourcecode:: http

      GET /calendars/15924213158245d0ad631c6a41a0e7c3/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "15924213158245d0ad631c6a41a0e7c3",
	"parent_id": "cea793f236334942bdae2c1e6c83607d",
	"PidTagSubject": "My sample appointment",
	"PidTagBody": "Sample body"
      },

   :reqheader Authorization: auth token
   :reqheader Accept: the response content depends on on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of the request
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:put:: /calendars/(id)/

   :synopsis: Set properties on the calendar item object identified by `id`

   **Example request**:

   .. sourcecode:: http

      PUT /calendars/15924213158245d0ad631c6a41a0e7c3/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "PidTagBody": "Sample body v2"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: The update was successfully applied
   :statuscode 400: Bad request


.. http:head:: /calendars/(id)/

   :synopsis: Check if the calendar item identified by `id` exists

   **Example request**:

   .. sourcecode:: http

      HEAD /calendars/15924213158245d0ad631c6a41a0e7c3/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:delete:: /calendars/(id)/

   :synopsis: Delete the calendar entry identified by `id`

   **Example request**:

   .. sourcecode:: http

      DELETE /calendars/15924213158245d0ad631c6a41a0e7c3 HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No content

   :reqheader Authorization: auth token
   :statuscode 204: Ok
   :statuscode 404: Item does not exist

.. http:head:: /calendars/(id)/attachments

   :synopsis: Retrieve the count of attachments within specified calendar

   **Example request**:

   .. sourcecode:: http

      HEAD /calendars/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      X-mapistore-rowcount: 2

   :reqheader Authorization: auth token
   :resheader X-mapistore-rowcount: The number of specified items within the calendar
   :statuscode 200: Ok


.. http:get:: /calendars/(id)/attachments

   :synopsis: List of attachments within specified calendar

   **Example request**:

   .. sourcecode:: http

      GET /calendars/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments?properties=id,PidTagAttachFilename HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": "2cc32afdcba1491d704d02c2eeda57ae3a9bd35e",
          "PidTagAttachFilename": "attach1.foo"
        },
        {
          "id": "d4d6301939fd0d832292c112925a1056a24f8b4e",
          "PidTagAttachFilename": "attach2.foo"
        },
        ...
      ]

   :>jsonarr string id: Attachment identifier
   :>jsonarr string PidTagAttachFilename: Attachment filename

   :query properties: Comma separated list of properties to return
                      for every calendar. If not set all properties will
                      be returned. E.g: ``id,PidTagAttachFilename``
   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :calendarheader:`Accept` header
   :resheader Content-Type: this depends on :calendarheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


Tasks
-----

.. http:post:: /tasks/

   :synopsis: Create a new task item and returns its ID

   **Example request**:

   .. sourcecode:: http

      POST /tasks/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "95fc55f35da743bc9450ae694f38def0",
        "PidTagSubject": "My sample task",
	"PidTagBody": "Sample body"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "b1f2726d32b44551b99f4a6adb61e112",
        "collection": "tasks"
      }

      :>json string id: Message identifier of the task item created
      :>json string collection: Collection the task belongs to
      :reqheader Authorization: auth token
      :statuscode 200: Ok


.. http:get:: /tasks/(id)/

   :synopsis: Retrieve all the properties of the task entry
              identified by `id`

   **Example request**:

   .. sourcecode:: http

      GET /tasks/b1f2726d32b44551b99f4a6adb61e112/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "b1f2726d32b44551b99f4a6adb61e112",
        "collection": "tasks",
        "parent_id": "95fc55f35da743bc9450ae694f38def0",
        "PidTagSubject": "My sample task",
        "PidTagBody": "Sample body"
      },

   :reqheader Authorization: auth token
   :reqheader Accept: the response content depends on on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of the request
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:put:: /tasks/(id)/

   :synopsis: Set properties on the task item object identified by `id`

   **Example request**:

   .. sourcecode:: http

      PUT /tasks/b1f2726d32b44551b99f4a6adb61e112/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "PidTagBody": "Sample body v2"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: The update was successfully applied
   :statuscode 400: Bad request


.. http:head:: /tasks/(id)/

   :synopsis: Check if the task item identified by `id` exists

   **Example request**:

   .. sourcecode:: http

      HEAD /tasks/b1f2726d32b44551b99f4a6adb61e112/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:delete:: /tasks/(id)/

   :synopsis: Delete the task entry identified by `id`

   **Example request**:

   .. sourcecode:: http

      DELETE /tasks/b1f2726d32b44551b99f4a6adb61e112 HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No content

   :reqheader Authorization: auth token
   :statuscode 204: Ok
   :statuscode 404: Item does not exist

.. http:head:: /tasks/(id)/attachments

   :synopsis: Retrieve the count of attachments within specified task

   **Example request**:

   .. sourcecode:: http

      HEAD /tasks/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      X-mapistore-rowcount: 2

   :reqheader Authorization: auth token
   :resheader X-mapistore-rowcount: The number of specified items within the task
   :statuscode 200: Ok


.. http:get:: /tasks/(id)/attachments

   :synopsis: List of attachments within specified task

   **Example request**:

   .. sourcecode:: http

      GET /tasks/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments?properties=id,PidTagAttachFilename HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": "2cc32afdcba1491d704d02c2eeda57ae3a9bd35e",
          "PidTagAttachFilename": "attach1.foo",
        },
        {
          "id": "d4d6301939fd0d832292c112925a1056a24f8b4e",
          "PidTagAttachFilename": "attach2.foo",
        },
        ...
      ]

   :>jsonarr string id: Attachment identifier
   :>jsonarr string PidTagAttachFilename: Attachment filename

   :query properties: Comma separated list of properties to return
                      for every task. If not set all properties will
                      be returned. E.g: ``id,PidTagAttachFilename``
   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :taskheader:`Accept` header
   :resheader Content-Type: this depends on :taskheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


Contacts
--------

.. http:post:: /contacts/

   :synopsis: Create a new contact item and returns its ID

   **Example request**:

   .. sourcecode:: http

      POST /contacts/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "9175fe8d54da416a9cb1a946c50b7467",
        "PidTagSubject": "My sample contact",
	"PidTagBody": "Sample body"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "d220314b8a374d2bbd7f43bf0819b5a0",
        "collection": "contacts"
      }

      :>json string id: Message identifier of the contact item created
      :>json string collection: Collection the contact belongs to
      :reqheader Authorization: auth token
      :statuscode 200: Ok


.. http:get:: /contacts/(id)/

   :synopsis: Retrieve all the properties of the contact entry
              identified by `id`

   **Example request**:

   .. sourcecode:: http

      GET /contacts/d220314b8a374d2bbd7f43bf0819b5a0/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "d220314b8a374d2bbd7f43bf0819b5a0",
        "collection": "contacts",
        "parent_id": "9175fe8d54da416a9cb1a946c50b7467",
        "PidTagSubject": "My sample contact",
        "PidTagBody": "Sample body"
      },

   :reqheader Authorization: auth token
   :reqheader Accept: the response content depends on on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of the request
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:put:: /contacts/(id)/

   :synopsis: Set properties on the contact item object identified by `id`

   **Example request**:

   .. sourcecode:: http

      PUT /contacts/d220314b8a374d2bbd7f43bf0819b5a0/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "PidTagBody": "Sample body v2"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: The update was successfully applied
   :statuscode 400: Bad request


.. http:head:: /contacts/(id)/

   :synopsis: Check if the contact item identified by `id` exists

   **Example request**:

   .. sourcecode:: http

      HEAD /contacts/d220314b8a374d2bbd7f43bf0819b5a0/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:delete:: /contacts/(id)/

   :synopsis: Delete the contact entry identified by `id`

   **Example request**:

   .. sourcecode:: http

      DELETE /contacts/d220314b8a374d2bbd7f43bf0819b5a0 HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No content

   :reqheader Authorization: auth token
   :statuscode 204: Ok
   :statuscode 404: Item does not exist

.. http:head:: /contacts/(id)/attachments

   :synopsis: Retrieve the count of attachments within specified contact

   **Example request**:

   .. sourcecode:: http

      HEAD /contacts/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      X-mapistore-rowcount: 2

   :reqheader Authorization: auth token
   :resheader X-mapistore-rowcount: The number of specified items within the contact
   :statuscode 200: Ok


.. http:get:: /contacts/(id)/attachments

   :synopsis: List of attachments within specified contact

   **Example request**:

   .. sourcecode:: http

      GET /contacts/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments?properties=id,PidTagAttachFilename HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": "2cc32afdcba1491d704d02c2eeda57ae3a9bd35e",
          "PidTagAttachFilename": "attach1.foo",
        },
        {
          "id": "d4d6301939fd0d832292c112925a1056a24f8b4e",
          "PidTagAttachFilename": "attach2.foo",
        },
        ...
      ]

   :>jsonarr string id: Attachment identifier
   :>jsonarr string PidTagAttachFilename: Attachment filename

   :query properties: Comma separated list of properties to return
                      for every contact. If not set all properties will
                      be returned. E.g: ``id,PidTagAttachFilename``
   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :contactheader:`Accept` header
   :resheader Content-Type: this depends on :contactheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


Notes
-----
.. http:post:: /notes/

   :synopsis: Create a new note item and returns its ID

   **Example request**:

   .. sourcecode:: http

      POST /notes/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "765dc8566f9e4baf94ee36e1b2763d50",
        "PidTagSubject": "My sample note",
	"PidTagBody": "Sample body"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "f07d68499c974a5bbffed5cc3ddcc31e",
        "collection": "notes"
      }

      :>json string id: Message identifier of the note item created
      :reqheader Authorization: auth token
      :statuscode 200: Ok


.. http:get:: /notes/(id)/

   :synopsis: Retrieve all the properties of the note entry
              identified by `id`

   **Example request**:

   .. sourcecode:: http

      GET /notes/f07d68499c974a5bbffed5cc3ddcc31e/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "f07d68499c974a5bbffed5cc3ddcc31e",
        "collection": "notes",
        "parent_id": "765dc8566f9e4baf94ee36e1b2763d50",
        "PidTagSubject": "My sample note",
        "PidTagBody": "Sample body"
      },

   :reqheader Authorization: auth token
   :reqheader Accept: the response content depends on on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of the request
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:put:: /notes/(id)/

   :synopsis: Set properties on the note item object identified by `id`

   **Example request**:

   .. sourcecode:: http

      PUT /notes/f07d68499c974a5bbffed5cc3ddcc31e/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "PidTagBody": "Sample body v2"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: The update was successfully applied
   :statuscode 400: Bad request


.. http:head:: /notes/(id)/

   :synopsis: Check if the note item identified by `id` exists

   **Example request**:

   .. sourcecode:: http

      HEAD /notes/f07d68499c974a5bbffed5cc3ddcc31e/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:delete:: /notes/(id)/

   :synopsis: Delete the note entry identified by `id`

   **Example request**:

   .. sourcecode:: http

      DELETE /notes/f07d68499c974a5bbffed5cc3ddcc31e HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No content

   :reqheader Authorization: auth token
   :statuscode 204: Ok
   :statuscode 404: Item does not exist

.. http:head:: /notes/(id)/attachments

   :synopsis: Retrieve the count of attachments within specified note

   **Example request**:

   .. sourcecode:: http

      HEAD /notes/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      X-mapistore-rowcount: 2

   :reqheader Authorization: auth token
   :resheader X-mapistore-rowcount: The number of specified items within the note
   :statuscode 200: Ok


.. http:get:: /notes/(id)/attachments

   :synopsis: List of attachments within specified note

   **Example request**:

   .. sourcecode:: http

      GET /notes/51c3187152d0a0daa5e0de4d6e3132cb561135e7/attachments?properties=id,PidTagAttachFilename HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": "2cc32afdcba1491d704d02c2eeda57ae3a9bd35e",
          "PidTagAttachFilename": "attach1.foo",
        },
        {
          "id": "d4d6301939fd0d832292c112925a1056a24f8b4e",
          "PidTagAttachFilename": "attach2.foo",
        },
        ...
      ]

   :>jsonarr string id: Attachment identifier
   :>jsonarr string PidTagAttachFilename: Attachment filename

   :query properties: Comma separated list of properties to return
                      for every note. If not set all properties will
                      be returned. E.g: ``id,type``
   :reqheader Authorization: auth token
   :reqheader Accept: the response content type depends on
                      :noteheader:`Accept` header
   :resheader Content-Type: this depends on :noteheader:`Accept`
                            header of request
   :statuscode 200: Ok
   :statuscode 404: Folder does not exist


Attachments
-----------

.. http:post:: /attachments/

   :synopsis: Create a new attachment item and return its ID

   **Example request**:

   .. sourcecode:: http

      POST /attachments/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "51c3187152d0a0daa5e0de4d6e3132cb561135e7",
        "PidTagAttachFilename": "sample attachment.foo",
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "12fd85ba7440cc17d2be3957c371c5d3b42270d0",
      }

      :>json string id: Message identifier of the attachment item created
      :reqheader Authorization: auth token
      :statuscode 200: Ok


.. http:get:: /attachments/(id)/

   :synopsis: Retrieve all the properties of the attachment entry
              identified by `id`

   **Example request**:

   .. sourcecode:: http

      GET /attachments/12fd85ba7440cc17d2be3957c371c5d3b42270d0/ HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "id": "12fd85ba7440cc17d2be3957c371c5d3b42270d0",
        "parent_id": "765dc8566f9e4baf94ee36e1b2763d50",
        "PidTagAttachFilename": "sample attachment.foo",
      },

   :reqheader Authorization: auth token
   :reqheader Accept: the response content depends on on
                      :mailheader:`Accept` header
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of the request
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:put:: /attachments/(id)/

   :synopsis: Set properties on the attachment item object identified by `id`

   **Example request**:

   .. sourcecode:: http

      PUT /attachments/12fd85ba7440cc17d2be3957c371c5d3b42270d0/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "PidTagDisplayName": "Sample"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: The update was successfully applied
   :statuscode 400: Bad request


.. http:head:: /attachments/(id)/

   :synopsis: Check if the attachment item identified by `id` exists

   **Example request**:

   .. sourcecode:: http

      HEAD /attachments/12fd85ba7440cc17d2be3957c371c5d3b42270d0/ HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK

   :reqheader Authorization: auth token
   :statuscode 200: Ok
   :statuscode 404: Item does not exist


.. http:delete:: /attachments/(id)/

   :synopsis: Delete the attachment entry identified by `id`

   **Example request**:

   .. sourcecode:: http

      DELETE /attachments/12fd85ba7440cc17d2be3957c371c5d3b42270d0 HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No content

   :reqheader Authorization: auth token
   :statuscode 204: Ok
   :statuscode 404: Item does not exist
