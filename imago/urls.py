from django.conf.urls import patterns, url
from imago.views import (JurisdictionList,
                         PeopleList,
                         VoteList,
                         EventList,
                         BillList,
                         OrganizationList,
                         DivisionList,
                         DisclosureList,

                         JurisdictionDetail,
                         PersonDetail,
                         EventDetail,
                         VoteDetail,
                         BillDetail,
                         OrganizationDetail,
                         DivisionDetail,
                         DisclosureDetail
                         )

urlpatterns = patterns(
    '',
    url(r'^jurisdictions/$', JurisdictionList.as_view()),
    url(r'^people/$', PeopleList.as_view()),
    url(r'^votes/$', VoteList.as_view()),
    url(r'^events/$', EventList.as_view()),
    url(r'^organizations/$', OrganizationList.as_view()),
    url(r'^bills/$', BillList.as_view()),
    url(r'^divisions/$', DivisionList.as_view()),
    url(r'^disclosures/$', DisclosureList.as_view()),

    # detail views
    url(r'^(?P<pk>ocd-jurisdiction/.+)/$', JurisdictionDetail.as_view()),
    url(r'^(?P<pk>ocd-person/.+)/$', PersonDetail.as_view()),
    url(r'^(?P<pk>ocd-event/.+)/$', EventDetail.as_view()),
    url(r'^(?P<pk>ocd-vote/.+)/$', VoteDetail.as_view()),
    url(r'^(?P<pk>ocd-organization/.+)/$', OrganizationDetail.as_view()),
    url(r'^(?P<pk>ocd-bill/.+)/$', BillDetail.as_view()),
    url(r'^(?P<pk>ocd-division/.+)/$', DivisionDetail.as_view()),
    url(r'^(?P<pk>ocd-disclosure/.+)/$', DisclosureDetail.as_view()),
)
