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

   :synopsis: Creates a new folder and returns its ID

   **Example request**:

   .. sourcecode:: http

      POST /folders/ HTTP/1.1
      Host: example.com
      Accept: application/json

      {
        "parent_id": "c7e77cc9999908ec54ae32f1faf17e0e",
        "name": "new folder name",
        "comment": "Comment about the folder"
      }

   :<json string parent_id: Parent Folder Identifier
   :<json string name: Name of the folder to create
   :<json string comment: Comment associated to the folder


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
	"name": "MyFolderName",
	"comment": "This is a sample folder"
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
         "name": "UpdatedFolderName"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 No Content

   :reqheader Authorization: auth token
   :statuscode 201: No Content
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
          "type": "email",
        },
        {
          "id": "fa21ee2b607ac6e327ecb39021be5469",
          "type": "calendar",
        },
        ...
      ]

   :>jsonarr string id: Message identifier
   :>jsonarr string type: Type of the message

   :query properties: List of wanted properties, response will only
                      contain these. If not set all properties will
                      be returned.
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
          "type": "folder",
        },
        {
          "id": "fa21ee2b607ac6e327ecb39021be5469",
          "type": "folder",
        },
        ...
      ]

   :>jsonarr string id: Folder identifier
   :>jsonarr string type: Type of the folder

   :query properties: List of wanted properties, response will only
                      contain these. If not set all properties will
                      be returned.
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


Emails
------
TBD

Calendars
---------
TBD

Tasks
-----
TBD

Attachments
-----------
TBD

Notes
-----
TBD
