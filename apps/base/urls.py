from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.base.views import BaseMixins, What_willMixins, SliderMixins, VideoMixins, BannerMixins, What_will_titleMixins, About_the_forumMixins, SliderTitleMixins, SliderSponsorsMixins, SliderTitleSponsorsMixins, ButtonMixins

router = DefaultRouter()

(
    router.register(r'logo', BaseMixins, basename='logo'),
    router.register(r'what_will', What_willMixins, basename='what_will'),
    router.register(r'slider', SliderMixins, basename='slider'),
    router.register(r'slider_title', SliderTitleMixins, basename='slider_sponsor'),
    router.register(r'slider_sponsor', SliderSponsorsMixins, basename='slider_sponsor'),
    router.register(r'slider_sponsor_title', SliderTitleSponsorsMixins, basename='slider_sponsor_title'),
    router.register(r'video', VideoMixins, basename='video'),
    router.register(r'banner', BannerMixins, basename='banner'),
    router.register(r'what_will_title', What_will_titleMixins, basename='what_will_title'),
    router.register(r'about_the_forum', About_the_forumMixins, basename='about_the_forum'),
    router.register(r'button', ButtonMixins, basename='button'),
)
urlpatterns = router.urls