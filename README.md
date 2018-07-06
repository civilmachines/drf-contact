# Django REST Framework Contact

**Contact App for Django REST Framework with API Views.**<br>

`Django REST Framework - Contact` is a Django App for creating user contacts. It's view are based upon
`Django REST Framework's GenericAPIView` and hence it contains a RESTful API views also.


I'll like to mention following names for certain contributions:

- **[Civil Machines Technologies Private Limited](https://github.com/civilmahines)**: For providing me platform and
funds for research work. This project is hosted currently with `CMT` only.
- [Himanshu Shankar](https://github.com/iamhssingh): For guiding me and providing me mentor-ship while doing this
project.

#### Installation

- Download and Install via `pip`
```
pip install drf_contact
```
or<br>
Download and Install via `easy_install`
```
easy_install drf_contact
```
- Add `drf_contact` in `INSTALLED_APPS`<br>
```
INSTALLED_APPS = [
    ...
    'drf_contact',
    ...
]
```
- Include urls of `drf_contact` in `urls.py`
```
urlpatterns = [
    ...
    path('api/contact/', include('drf_contact.urls')),
    ...
]

# or

urlpatterns = [
    ...
    url(r'^api/contact/', include('drf_contact.urls')),
    ...
]
```

- Finally, run `migrate` command
```
python manage.py migrate drf_contact
```