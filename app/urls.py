from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm,MySetPasswordForm

urlpatterns = [
    path('', views.home ),
    path('about/', views.About, name='about' ),
    path('contact', views.Contact, name='contact' ),
    path('category/<slug:val>', views.Category.as_view(), name = 'category' ),
    path('category-title/<val>', views.CategoryTitle.as_view(), name = 'category-title' ),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name = 'product-detail' ),
    path("profile/", views.ProfileView.as_view(), name = 'profile'),
    path("address/", views.Address, name = 'address'),
    path('address-update/<int:pk>', views.AddressUpdate.as_view(), name = 'address-update' ),

    #Add to cart
    path('add-to-cart/', views.AddToCart, name = 'add_to_cart'),
    path('cart/', views.ShowCart, name = 'cart'),
    path('checkout/', views.CheckOut.as_view(), name = 'checkout'),
    path('paymentdone/', views.PaymentDone, name = 'paymentdone'),
    path('orders/', views.Orders, name = 'orders'),
    path('search/', views.Search, name = 'search'),
    path('wishlist/', views.ShowWishlist, name = 'wishlist'),



    # Add to cart or Quantity + - and remove from cart
    path('pluscart/',views.PlusCart),
    path('minuscart/',views.MinusCart),
    path('removecart/',views.RemoveCart),
    path('pluswishlist/',views.PlusWishlist),
    path('minuswishlist/',views.MinusWishlist),


    #Login Authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name = 'customer-registration' ),
    path('account/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), 
        name = 'login' ),
    #Change password
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='app/change_password.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name = 'passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name = 'logout' ), # Ek liner code 'logout' er jonno

    # Password reset-Forgot password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name = 'password_reset' ),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name = 'password_reset_done' ),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class= MySetPasswordForm), name = 'password_reset_confirm' ),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name = 'password_reset_complete' ),



    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # #  Media, Template, Static Files er jonno ei 2 line code er sate ei line tuku add korte hobe. join code er bikolpo.

admin.site.site_header = 'My shopping'    # Django admin pannel decorated
admin.site.site_title = 'My shopping'
admin.site.site_index_title = ' Welcome to My shopping'