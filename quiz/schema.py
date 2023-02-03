import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Quiz, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ("id", "title", "category")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query(graphene.ObjectType):

    all_quizzes = DjangoListField(QuizType)
    # To get a quiz
    quiz = graphene.Field(QuizType, id=graphene.Int())

    all_questions = graphene.List(QuestionType)
    # To get a question
    question = graphene.Field(QuestionType, id=graphene.Int())

    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_quiz(self, info, id):
        return Quiz.objects.get(pk=id)

    def resolve_question(self, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_questions(self, info):
        return Question.objects.all()

    def resolve_all_answers(self, info, id):
        return Answer.objects.filter(question=id)


schema = graphene.Schema(query=Query)
