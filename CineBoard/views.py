from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from . import models
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegisterView(generic.CreateView):
    template_name = 'movies/register.html'
    form_class = UserCreationForm
    success_url = '/user_login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuthLoginView(LoginView):
    template_name = 'movies/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return '/movie_list/'


class AuthLogoutView(LogoutView):
    next_page = '/user_login/'


class MovieListView(generic.ListView):
    template_name = 'movies/movie_list.html'
    model = models.Movie
    context_object_name = 'movies'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset().order_by("-id")

        genre_id = self.request.GET.get("genre_id")
        if genre_id:
            queryset = queryset.filter(genre__id=genre_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = context["page_obj"]
        context["genres"] = models.Genre.objects.all()
        return context

class MovieDetailView(generic.DetailView):
    template_name = 'movies/movie_detail.html'
    model = models.Movie
    context_object_name = 'movie'
    pk_url_kwarg = 'id'

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')

        return context

class SearchView(generic.ListView):
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.filter(movie_title__icontains=self.request.GET.get('s'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Comment
    fields = ["comment_text"]
    login_url = "/user_login/"

    def form_valid(self, form):
        form.instance.movie_id = self.kwargs["id"]
        form.instance.commentator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return f'/movie_list/{self.kwargs["id"]}/'


class VipBookingCreateView(LoginRequiredMixin, generic.View):
    login_url = "/user_login/"

    def post(self, request, *args, **kwargs):
        movie_id = self.kwargs["id"]

        user_has_booking = models.VipBooking.objects.filter(user=request.user).exists()

        if not user_has_booking:
            seat = request.POST.get("seat_number", 1)
            models.VipBooking.objects.create(
                movie_id=movie_id,
                user=request.user,
                seat_number=int(seat)
            )

        return redirect(f'/movie_list/{movie_id}/')


class MovieCreateView(generic.CreateView):
    template_name = "movies/create_movie.html"
    model = models.Movie
    fields = [
        "genre",
        "movie_title",
        "description",
        "image",
        "director",
        "rating",
        "budget",
        "release_date",
        "age_limit",
        "country",
    ]
    success_url = "/movie_list/"


class MovieUpdateView(generic.UpdateView):
    template_name = "movies/update_movie.html"
    model = models.Movie
    fields = [
        "genre",
        "movie_title",
        "description",
        "image",
        "director",
        "rating",
        "budget",
        "release_date",
        "age_limit",
        "country",
    ]
    pk_url_kwarg = "id"

    def get_success_url(self):
        return f'/movie_list/{self.object.id}/'


class MovieDeleteView(generic.DeleteView):
    template_name = "movies/movie_confirm_delete.html"
    model = models.Movie
    pk_url_kwarg = "id"
    success_url = "/movie_list/"