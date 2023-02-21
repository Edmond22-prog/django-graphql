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


class PersonType(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()
    
    def resolve_full_name(parent, info):
        return f"{parent.first_name} {parent.last_name}"


class Query(graphene.ObjectType):
    me = graphene.Field(PersonType, first_name=graphene.String(), last_name=graphene.String())

    all_quizzes = DjangoListField(QuizType)
    # To get a quiz
    quiz = graphene.Field(QuizType, id=graphene.Int())

    all_questions = graphene.List(QuestionType)
    # To get a question
    question = graphene.Field(QuestionType, id=graphene.Int())

    all_answers = graphene.List(AnswerType, id=graphene.Int())
    
    def resolve_me(parent, info, first_name, last_name):
        return PersonType(first_name=first_name, last_name=last_name)

    def resolve_quiz(parent, info, id):
        return Quiz.objects.get(pk=id)

    def resolve_question(parent, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_questions(parent, info):
        return Question.objects.all()

    def resolve_all_answers(parent, info, id):
        return Answer.objects.filter(question=id)


schema = graphene.Schema(query=Query)
