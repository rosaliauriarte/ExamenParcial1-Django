from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import TipoDocumento, tipoSeguro,Paciente,Especialidades,Doctores,Citas
from django import forms

# Create your views here.
def home(request):
    # print('Hola mundo')
    return render(request, 'home.html')

class documentoList(ListView):
    model = TipoDocumento
    context_object_name = "tipodocumento"
    template_name = "citas/documento_list.html"
    
class documentoCreate(CreateView):
    model = TipoDocumento
    fields = ["nombre"]
    success_url = reverse_lazy("tipodocumento")
    template_name = "citas/documento_form.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El documento fue creado correctamente.")
        return super(documentoCreate, self).form_valid(form)

class documentoUpdate(UpdateView):
    model = TipoDocumento
    fields = ["nombre"]
    success_url = reverse_lazy("tipodocumento")
    template_name = "citas/documento_form.html"

    def form_valid(self, form):
        messages.success(self.request, "El documento fue actualizado correctamente.")
        return super(documentoUpdate, self).form_valid(form)
    
class documentoDelete(DeleteView):
    model = TipoDocumento
    success_url = reverse_lazy("tipodocumento")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El documento fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class seguroList(ListView):
    model = tipoSeguro
    context_object_name = "tiposeguro"
    template_name = "citas/seguro_list.html"
    
class seguroCreate(CreateView):
    model = tipoSeguro
    fields = ["nombre"]
    success_url = reverse_lazy("tiposeguro")
    template_name = "citas/seguro_form.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El Seguro fue creado correctamente.")
        return super(seguroCreate, self).form_valid(form)

class seguroUpdate(UpdateView):
    model = tipoSeguro
    fields = ["nombre"]
    success_url = reverse_lazy("tiposeguro")
    template_name = "citas/seguro_form.html"

    def form_valid(self, form):
        messages.success(self.request, "El Seguro fue actualizado correctamente.")
        return super(seguroUpdate, self).form_valid(form)
    
class seguroDelete(DeleteView):
    model = tipoSeguro
    success_url = reverse_lazy("tiposeguro")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El Seguro fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class pacienteList(ListView):
    model = Paciente
    context_object_name = "paciente"
    template_name = "citas/paciente_list.html"

 
    
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["nombres", "apellidos", "direccion","nDocumento", "fechaNacimiento", "tiposeguro", "tipodocumento"]
        template_name = "citas/paciente_form.html"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tiposeguro'].label_from_instance = lambda obj: obj.tipo_seguro_nombre
        self.fields['tipodocumento'].label_from_instance = lambda obj: obj.tipo_documento_nombre

class pacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy("paciente")
    template_name = "citas/paciente_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El paciente fue creado correctamente.")
        return super().form_valid(form)
    
class pacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy("paciente")

    def form_valid(self, form):
        messages.success(self.request, "El paciente fue actualizado correctamente.")
        return super(pacienteUpdate, self).form_valid(form)
    
class pacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy("paciente")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El paciente fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class especialidadesList(ListView):
    model = Especialidades
    context_object_name = "especialidades"
    template_name = "especialidades_list.html"
    
class especialidadesCreate(CreateView):
    model = Especialidades
    fields = ["nombre"]
    success_url = reverse_lazy("especialidades")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La especialidad fue creado correctamente.")
        return super(especialidadesCreate, self).form_valid(form)
    
class especialidadesUpdate(UpdateView):
    model = Especialidades
    fields = ["nombre"]
    success_url = reverse_lazy("especialidades")

    def form_valid(self, form):
        messages.success(self.request, "La especialidad fue actualizado correctamente.")
        return super(especialidadesUpdate, self).form_valid(form)
    
class especialidadesDelete(DeleteView):
    model = Especialidades
    success_url = reverse_lazy("especialidades")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "La especialidad fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class doctorList(ListView):
    model = Doctores
    context_object_name = "doctores"
    template_name = "citas/doctor_list.html"
    
class doctorCreate(CreateView):
    model = Doctores
    fields = ["nombre","direccion","telefono"]
    success_url = reverse_lazy("doctores")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El doctor fue creado correctamente.")
        return super(doctorCreate, self).form_valid(form)
    
class doctorUpdate(UpdateView):
    model = Doctores
    fields = ["nombre","direccion","telefono"]
    success_url = reverse_lazy("doctores")

    def form_valid(self, form):
        messages.success(self.request, "El doctor fue actualizado correctamente.")
        return super(doctorUpdate, self).form_valid(form)
    
class doctorDelete(DeleteView):
    model = Doctores
    success_url = reverse_lazy("doctores")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El doctor fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class citasList(ListView):
    model = Citas
    context_object_name = "citas"
    template_name = "citas/citas_list.html"


class citasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ["fechaCita","observaciones",  "especialidad", "doctor", "paciente"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['especialidad'].label_from_instance = lambda obj: obj.especialidad_nombre
        self.fields['doctor'].label_from_instance = lambda obj: obj.nombre_doctor
        self.fields['paciente'].label_from_instance = lambda obj: obj.nombres


class citasCreate(CreateView):
    model = Citas
    form_class = citasForm
    success_url = reverse_lazy("citas")
    template_name = "citas/citas_form.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La cita fue creado correctamente.")
        return super().form_valid(form)
    
class citasUpdate(UpdateView):
    model = Citas
    form_class = citasForm
    success_url = reverse_lazy("citas")

    def form_valid(self, form):
        messages.success(self.request, "La cita fue actualizado correctamente.")
        return super(citasUpdate, self).form_valid(form)
    
class citasDelete(DeleteView):
    model = Citas
    success_url = reverse_lazy("citas")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "La cita fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    