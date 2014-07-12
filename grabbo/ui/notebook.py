
NOTEBOOK_UI = ''''''

TAB_UI = '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.18.3 -->
<interface>
  <requires lib="gtk+" version="3.10"/>
  <object class="GtkImage" id="CloseIcon">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="icon_name">window-close</property>
  </object>
  <object class="GtkImage" id="TabIcon">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="icon_name">applications-internet</property>
  </object>
  <object class="GtkBox" id="box">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <child>
      <object class="GtkButton" id="TabButton">
        <property name="label" translatable="yes">Tab</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="halign">start</property>
        <property name="valign">start</property>
        <property name="image">TabIcon</property>
        <property name="relief">none</property>
      </object>
      <packing>
        <property name="expand">False</property>
        <property name="fill">False</property>
        <property name="position">0</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="Close">
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="halign">start</property>
        <property name="valign">start</property>
        <property name="image">CloseIcon</property>
        <property name="relief">none</property>
      </object>
      <packing>
        <property name="expand">False</property>
        <property name="fill">False</property>
        <property name="position">1</property>
      </packing>
    </child>
  </object>
</interface>
'''
