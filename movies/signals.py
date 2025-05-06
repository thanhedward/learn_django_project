from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie
from projects.models import Project
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Movie)
def create_movie_project(sender, instance, created, **kwargs):
    logger.info(f"Signal triggered for movie: {instance.title}")
    if created:
        logger.info(f"Creating new project for movie: {instance.title}")
        try:
            project = Project.objects.create(
                name=f"Movie Production: {instance.title}",
                description=f"Production project for the movie {instance.title} ({instance.year}). Genre: {instance.genre}",
                owner=instance.creator,
                status='PENDING'
            )
            logger.info(f"Successfully created project: {project.name}")
        except Exception as e:
            logger.error(f"Error creating project: {str(e)}")