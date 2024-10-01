from flask_wtf import FlaskForm
from wtforms import StringField, Field, SubmitField
from flask import Flask, render_template
from wtforms.widgets import TextInput

app = Flask(__name__)
app.config['SECRET_KEY'] = "laiweuhf"


# Create Custom "Tag" Field for Concepts
class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return ', '.join(self.data)
        else:
            return ''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []


# Test Form
class MyForm(FlaskForm):
    name = StringField('Name')
    tags = TagListField('Tags')
    submit = SubmitField('Submit')


@app.route('/', methods=["GET", "POST"])
def home():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data,
        tags = form.tags.data
        print(name)
        print(tags)
        return 'Tags:{}'.format(tags)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5010)