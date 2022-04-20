import graphene


class UpdateStatus(graphene.Mutation):
    class Arguments:
        status = graphene.String()  # input field

    ok = graphene.Boolean()  # output field

    # root - schema, info - request, user etc., status - input field
    def mutate(root, info, status):
        print('info: ', info)
        print('info.context: ', info.context)
        print('info.context.user: ', info.context.user)
        user = info.context.user
        user.status = status
        return UpdateStatus(ok=True)


class ProfileMutation(graphene.ObjectType):
    change_status = UpdateStatus.Field()
